from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('classes/', views.all_classes, name='classes'),
    path('programs/', views.all_programs, name='programs'),
    path('<class_id>', views.class_details, name='class_details'),
]