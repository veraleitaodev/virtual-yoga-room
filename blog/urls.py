from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:question_id>/', views.blog_details, name='blog_details'),
]
