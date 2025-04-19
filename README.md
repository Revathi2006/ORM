# Ex02 Django ORM Web Application
## Date: 09:04:25
## AIM
To develop a Django application to store and retrieve data from a Students Database using Object Relational Mapping(ORM).

 ## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from.models import Student,StudentAdmin
admin.site.register(Student,StudentAdmin)


models.py
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

```
## OUTPUT
![alt text](<Screenshot (65).png>)

## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
