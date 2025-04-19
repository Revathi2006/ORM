
from django.db import models
from django.contrib import admin
class Student(models.Model):
    sid=models.CharField(max_length=20,help_text="Student Id")
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
class StudentAdmin(admin.ModelAdmin):
    list_display=('sid','name','rollno','age','email')


# Create your models here.
