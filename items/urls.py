from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('lectures/', views.all_lectures, name='lectures'),
    path('programs/', views.all_programs, name='programs'),
    path('lectures/<int:lecture_id>', views.lecture_details, name='lecture_details'),
    path('programs/<int:program_id>',
         views.program_details, name='program_details'),
]
