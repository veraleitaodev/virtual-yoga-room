from django.shortcuts import render


def blog(request):
    return render(request, 'blog/blog.html')


def post_details(request):
    return render(request, 'blog/post-details.html')
