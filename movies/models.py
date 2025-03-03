"""
This module contains model definitions for the Blog application.
"""
from django.db import models

# Create your models here.
class Movie(models.Model):
    """
    Represents a movie with various attributes such as title, director, release date, genre, and duration.
    """
    #each class vairable represents a database i.e. table fiels in the model"""
    #index_id = models.FloatField(unique=True, db_index=True)
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=30)
    release_date = models.DateTimeField('release date')
    genre = models.CharField(max_length=200)
    duration = models.FloatField()
    def __str__(self):
        return f"{self.title} - {self.director}"
    @property
    def is_post_production_completed(self):
        return self.duration > 0