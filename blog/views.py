from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import CommentForm


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog-details.html', context)



def add_comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('blog/blog-details.html')
    form = CommentForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/add-comment.html', context)
