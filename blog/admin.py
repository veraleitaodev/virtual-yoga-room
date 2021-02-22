from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'date',
        'author'
    )

    ordering = ['date']


admin.site.register(Blog, BlogAdmin)
