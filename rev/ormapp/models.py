from django.db import models
from django.contrib import admin
class Movie(models.Model):
 
    Moviename=models.CharField(max_length=100)
    Actor=models.CharField(max_length=100)
    Rating=models.FloatField()
    Releaseyear=models.IntegerField()
class MovieAdmin(admin.ModelAdmin):
    list_display=('Moviename','Actor','Rating','Releaseyear')