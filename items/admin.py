from django.contrib import admin
from .models import Class, Program


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
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


admin.site.register(Class, ClassAdmin)
admin.site.register(Program, ProgramAdmin)
