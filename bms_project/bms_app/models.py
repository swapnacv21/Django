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

    def __str__(self):
        return self.movie_name

class Language(models.Model):
    movie_language=models.TextField()

class Movie_lang(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    lang=models.ForeignKey(Language,on_delete=models.CASCADE)

class members(models.Model):
    name=models.TextField()
    img=models.FileField()
    position=models.TextField()
    cast=models.BooleanField(default=False)
    crew=models.BooleanField(default=False)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)




