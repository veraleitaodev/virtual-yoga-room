from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('classes/', views.all_classes, name='classes'),
    path('programs/', views.all_programs, name='programs'),
    path('classes/<int:class_id>', views.class_details, name='class_details'),
    path('programs/<int:program_id>',
         views.program_details, name='program_details'),
]
