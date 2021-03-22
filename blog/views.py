from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Blog, Comment
from .forms import CommentForm


def all_blogs(request):
    """ A view to render all blogs into blogs template """
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comments.filter(active=True).order_by("-date")
    comment_form = CommentForm()

    return render(request, 'blog/blog-details.html', {
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form,
    })


def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    new_comment = None
    comment_form = CommentForm()

    # comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            try:
                # Create Comment object but does not save to db
                new_comment = comment_form.save(commit=False)
                # checks user is the one making the comments
                new_comment.user = request.user
                # assign the current blog to the comment
                new_comment.blog = blog
                # save the comment to the db
                new_comment.save()
                return redirect('blog/blog-details.html')
            except ValueError:
                messages.error(
                    request, 'Invalid information. Please try again.')
        else:
            comment_form = CommentForm()

    context = {
        'blog': blog,
        'comment_form': comment_form,
        'new_comment': new_comment
    }
    template = ('blog/blog-details.html')
    return render(request, template, context)


def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment_form = CommentForm(instance=comment)

    try:
        if comment_form.is_valid():
            # Updates extisting Comment
            comment_form = CommentForm(request.POST, instance=comment)
            # checks user is the one making the comments
            comment_form.user = request.user
            # save the comment to the db
            comment_form.save()
            return redirect('blog/blog-details.html')

        except ValueError:
                messages.error(
                    request, 'Invalid information. Please try again.')
    else:
        comment_form = CommentForm(instance=comment)

    context = {
        'comment': comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/comment-update.html', context)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    context = {
        'comment': comment,
    }

    return render(request, 'blog/blog-details.html', context)
