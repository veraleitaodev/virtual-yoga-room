from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_details(request):
    return render(request, 'blog/blog-details.html')
