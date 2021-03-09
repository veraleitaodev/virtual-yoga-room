from django.contrib import admin
from .models import Tag, Program, Class


class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'number_classes',
        'rating',
        'instructor'
    )

    ordering = ('sku',)


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'program',
        'rating',
        'instructor'
    )

    ordering = ('sku',)


admin.site.register(Program, ProgramAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Tag)
