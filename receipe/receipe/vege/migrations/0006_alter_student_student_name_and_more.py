# Generated by Django 4.2 on 2023-06-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_department_studentid_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentid',
            name='student_id',
            field=models.CharField(max_length=1000),
        ),
    ]