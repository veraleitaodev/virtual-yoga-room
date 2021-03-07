from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.blog_details, name='blog_details'),
    path('<int:blog_id>/add_comment', views.blog_details, name='add_comment'),
]
