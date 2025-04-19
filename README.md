# Ex02 Django ORM Web Application
## Date: 09:04:25
## AIM
To develop a Django application to store and retrieve data from a movies Database using Object Relational Mapping(ORM).

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
models.py
from django.db import models
from django.contrib import admin
class Movie(models.Model):
 
    Moviename=models.CharField(max_length=100)
    Actor=models.CharField(max_length=100)
    Rating=models.FloatField()
    Releaseyear=models.IntegerField()
    
class MovieAdmin(admin.ModelAdmin):
    list_display=('Moviename','Actor','Rating','Releaseyear')

admin.py

from django.contrib import admin
from.models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

```
## OUTPUT
![alt text](<Screenshot (66).png>)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
