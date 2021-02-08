from django.contrib import admin
from .models import Class, Category, Program


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'program',
        'video',
        'image',
        'image_url',
        'description',
        'rating',
        'instructor'
    )

    ordering = ('sku',)


class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'number_classes',
        'image',
        'image_url',
        'description',
        'rating',
        'instructor'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Class, ClassAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Program, ProgramAdmin)
