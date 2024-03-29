from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
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
                return redirect(reverse('blog:blog_details', args=[blog.id]))
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


@login_required
def update_comment(request, comment_id, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)

    if request.method == 'GET':
        comment_form = CommentForm(instance=comment)
        return render(request, 'blog/comment-update.html',
                      {'comment_form': comment_form})
    else:
        try:
            comment_form = CommentForm(
                request.POST, instance=comment)
            comment_form.save()
            return redirect(reverse('blog:blog_details', args=[blog.id]))
        except ValueError:
            messages.error(
                request, 'Invalid information. Please try again.')
            return render(request, 'blog/comment-update.html',
                          {
                            'comment': comment,
                            'comment_form': comment_form,
                          })


@login_required
def delete_comment(request, comment_id, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment deleted!')
        return redirect(reverse('blog:blog_details', args=[blog.id]))
