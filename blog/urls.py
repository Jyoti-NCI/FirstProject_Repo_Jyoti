"""
URL configuration for the Blog application.
"""
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name='create'),
    path('<int:blog_id>/', views.show, name = 'show'),
    path('<int:blog_id>/delete/', views.delete, name = 'delete'),
    ]
    