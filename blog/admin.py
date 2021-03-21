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
    readonly_fields = ('date',)

    list_display = (
        'blog',
        'username',
        'active'
    )
    list_filter = ('active', 'date')
    search_fields = ('username', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
