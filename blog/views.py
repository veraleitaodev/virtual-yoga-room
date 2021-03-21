from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from .models import Blog
from .forms import CommentForm


def all_blogs(request):
    """ A view to render all blogs into blogs template """
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_details(request, blog_id):
    """ A view to display blog details """
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comments.filter(active=True).order_by("-date")
    comment_form = CommentForm()
    context = {
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'blog/blog-details.html', context)


def add_comment(request):
    new_comment = None
    comment_form = CommentForm()

    # comment posted
    if request.method == 'POST':

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Create Comment object but does not save to db
            new_comment = comment_form.save(commit=False)
            # assign the current user to the comment
            new_comment.user = request.user
            # save the comment to the db
            new_comment.save()
        else:
            comment_form = CommentForm()

    return redirect(reverse('blog_details', args=[new_comment.id]))
