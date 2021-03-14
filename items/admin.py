from django.contrib import admin
from .models import Tag, Program, Lecture


class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'number_lectures',
        'rating',
        'instructor'
    )

    ordering = ('sku',)


class LectureAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'program',
        'rating',
        'instructor'
    )

    ordering = ('sku',)


admin.site.register(Program, ProgramAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Tag)
