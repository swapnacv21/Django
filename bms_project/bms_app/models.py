from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    movie_name=models.TextField()
    bg_img=models.FileField()
    fg_img=models.FileField()
    duration=models.TextField()
    category=models.TextField()
    date=models.DateField()

class Language(models.Model):
    movie_language=models.TextField()

class Movie_lang(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    lang=models.ForeignKey(Language,on_delete=models.CASCADE)




