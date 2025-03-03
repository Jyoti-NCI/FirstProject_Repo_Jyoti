"""
This module contains model definitions for the Blog application.
"""
from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    Represents a blog with various attributes such as title, director, publish_date, blog_type, and content.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    publish_date = models.DateTimeField('publish date')
    blog_type = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    def str (self):
        """Returns a string representation of the blog instance."""
        return self.title + " - " + self.author
    @property
    def is_post_production_completed(self):
        """Checks if the post-production process is completed based on content."""
        return bool(self.content)
        