from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import CommentForm


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comments.filter(active=True)
    new_comment = None
    # comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():

            # Create Comment object but does not save to db
            new_comment = comment_form.save(commit=False)
            # assign the current blog to the comment
            new_comment.blog = blog
            # save the comment to the db
            new_comment.save()
        else:
            comment_form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    return render(request, 'blog/blog-details.html', context)
