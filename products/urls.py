from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_classes, name='classes'),
    path('', views.all_programs, name='programs'),
    path('<class_id>', views.class_details, name='class_details'),
]