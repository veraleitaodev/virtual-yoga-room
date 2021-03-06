from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog-details.html', {'blog': blog})


def add_comments(request):
    new_comment = request.POST.get('new_comment')
    author = request.POST.get('comment_author')
    Comment.objects.create(new_comment=new_comment, author=author)

    return redirect('blog/blog-details.html')
    return render(request, 'blog/add-comment.html')
