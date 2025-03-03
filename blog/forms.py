"""
This module contains form definitions for the Blog application.
"""
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    """Form for creating and updating Blog instances."""
    class Meta:
        """Meta configuration for BlogForm."""
        model = Blog
        fields = ['title', 'author', 'publish_date', 'blog_type', 'content']
        