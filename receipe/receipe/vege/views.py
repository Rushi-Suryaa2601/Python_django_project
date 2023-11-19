from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings
# Create your views here.

@login_required(login_url='/login/')
def recepes(request):
    if request.method=="POST":
        data=request.POST
        recepe_name=data.get('recepe_name')
        recepe_desc=data.get('recepe_desc')
        recepe_image=request.FILES.get('recepe_image')
        
        print(recepe_name)
        print(recepe_desc)
        print(recepe_image)
        recepe.objects.create(
            recepe_name=recepe_name,
            recepe_desc=recepe_desc,
            recepe_image=recepe_image,
            )
        return redirect('/')
    queryset=recepe.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(recepe_name__icontains=request.GET.get('search'))

        
    context={'receipes':queryset}
    # print(context)

    return render(request,'receipes.html',context)

@login_required(login_url='/login/')
def delete_recepe(request,id):
    queryset=recepe.objects.get(id=id)
    queryset.delete()

    return redirect('/')

def update_recepe(request,id):
    queryset=recepe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        recepe_name=data.get('recepe_name')
        recepe_desc=data.get('recepe_desc')
        recepe_image=request.FILES.get('recepe_image')

        queryset.recepe_name=recepe_name
        queryset.recepe_desc=recepe_desc
        if recepe_image:
            queryset.recepe_image=recepe_image

        queryset.save()
        return redirect('/')

        

    context={'receipes':queryset}
    return render(request,'update_recepe.html',context)


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalis Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')
def register_page(request):
    if request.method != "POST":
        return render(request,'register.html')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    username=request.POST.get('username')
    password=request.POST.get('password')

    user=User.objects.filter(username=username)
    if user.exists():
        messages.info(request,'Username alreadty taken')
        return redirect('/register/')

    user=User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        # password=password, in this format it does not save password in encrypt format so we have to use set_password method
    )
    user.set_password(password)
    user.save()
    messages.info(request,"Account created successfully")
    return redirect('/login/')



from django.db.models import Q,Sum


@login_required(login_url='/login/')
def get_student(request):
    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(student_email__icontains=search)
                                 
                                 )

    
    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'queryset':page_obj}

    return render(request,'report/students.html',context)

from .seed import generete_report_card
@login_required(login_url='/login/')
def see_marks(request,student_id):
    # generete_report_card()
    queryset=Subject_marks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))

    return render(request,'report/see_marks.html',{'queryset':queryset,'total_marks':total_marks})



from django.core.mail import EmailMessage


def send_email(request):
    subject = "Hello from Django"
    body = "This is the body of the email."
    sender = "rushisuryagandh4455@gmail.com"
    recipient = "rushisuryagandh4455@gmail.com"
    file_path=f"{settings.BASE_DIR}/main.xlsx"
    # Create an EmailMessage object
    email = EmailMessage(subject, body, sender, [recipient])
    email.attach_file(file_path)

 
    # Send the email
    email.send()

    return redirect('/')
