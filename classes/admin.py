from django.contrib import admin
from .models import Class, Category


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'videos',
        'image',
        'image_url',
        'description',
        'rating'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Class, ClassAdmin)
admin.site.register(Category, CategoryAdmin)
