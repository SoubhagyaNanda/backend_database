from django.db import models

# Create your models here.

class Marvel(models.Model):
    movie_base= models.CharField(max_length= 100, primary_key=True)

    def __str__(self):
        return self.movie_base

class Movies(models.Model):
    movie_base=models.ForeignKey(Marvel, on_delete= models.CASCADE)
    movie_name=models.CharField(max_length=100, primary_key=True)
    Relese_date= models.DateField(auto_now=True)
    Ott= models.URLField(default='http//netflix.com')

    def __str__(self):
        return self.movie_name

class Actor(models.Model):
    movie_name=models.ForeignKey(Movies, on_delete=models.CASCADE)
    character = models.CharField(max_length=100)

    def __str__(self):
        return self.character