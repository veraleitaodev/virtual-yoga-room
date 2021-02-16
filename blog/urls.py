from django.urls import path

from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:question_id>/', views.post_details, name='post_detail'),
]