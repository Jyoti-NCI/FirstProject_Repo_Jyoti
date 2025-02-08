from django.db import models

# Create your models here.
class Movie(models.Model):
    #each class vairable represents a database i.e. table fiels in the model
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=30)
    release_date = models.DateTimeField('release date')
    genre = models.CharField(max_length=200)
    duration = models.FloatField()