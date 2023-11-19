from django.contrib import admin
from django.db.models import Sum

# Register your models here.
from .models import *

admin.site.register(recepe)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentId)
admin.site.register(Subject)

class Subject_marksAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']

admin.site.register(Subject_marks,Subject_marksAdmin)


class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks','data_of_reportcard_generation']
    ordering=['student_rank']
    def total_marks(self,obj):
        subject_marks=Subject_marks.objects.filter(student=obj.student)
        marks= (subject_marks.aggregate(marks=Sum('marks')))
        return marks['marks']

admin.site.register(ReportCard,ReportCardAdmin)