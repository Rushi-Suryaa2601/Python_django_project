from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class recepe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recepe_name=models.CharField(max_length=150)
    recepe_desc=models.TextField()
    recepe_image=models.ImageField(upload_to="recepe_img")
    recepe_view_count=models.IntegerField(default=1)

class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class meta:
        ordering=['department']


class StudentId(models.Model):
    student_id=models.CharField(max_length=1000)
    def __str__(self)->str:
       return self.student_id

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)   

    def __str__(self) -> str:
        return self.subject_name   

class Student(models.Model):
    department=models.ForeignKey(Department,related_name='depart',on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentId,related_name='studentid',on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=10)
    student_address=models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class meta:
        ordering=['student_name']
        verbose_name='student'

class Subject_marks(models.Model):
    student=models.ForeignKey(Student,related_name='studentmarks',on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'

    class meta:
        unique_together=['student','subject']

class ReportCard(models.Model):
    student=models.ForeignKey(Student,related_name="studentreportcard",on_delete=models.CASCADE)  
    student_rank=models.IntegerField()
    data_of_reportcard_generation=models.DateField(auto_now_add=True)


    class meta:
        unique_together=['student_rank','data_of_reportcard_generation']


