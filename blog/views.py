"""
This module contains view functions for the blog application.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Blog
from django.http import Http404
from .forms import BlogForm
from django.utils import timezone


def create(request):
    """Handles the creation of a new blog post."""
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            new_blog = form.save(commit=False)
            new_blog.publish_date = timezone.now()  # Set the publish date to now
            new_blog.save()
            return redirect('blog:index')  # Redirect to the index page after creation
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})

def index(request):
    """Displays the list of the latest 15 blog posts."""
    newest_blog = Blog.objects.order_by('-publish_date')[:15]
    context = {'newest_blog': newest_blog}
    return render(request, 'blog/index.html', context)
def show(request, blog_id):
    """Displays the details of a specific blog post."""
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/show.html', {'blog':blog})
def delete(request, blog_id):
    """Deletes a specific blog post and redirects to the index."""
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return render('blog:index')

