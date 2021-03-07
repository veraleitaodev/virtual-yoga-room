from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'date',
        'author'
    )

    ordering = ['date']


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment',
        'name',
        'date'
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
