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
    readonly_fields = ('date', 'user', 'blog', 'comment')

    list_display = (
        'blog',
        'active',
        'date',
        'user',
        'id',
    )
    list_filter = ('active', 'date')
    search_fields = ('user', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
