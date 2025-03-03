"""
Admin configuration for the Blog app.
"""
from django.contrib import admin

# Register your models here.
from . models import Blog
admin.site.register(Blog)
