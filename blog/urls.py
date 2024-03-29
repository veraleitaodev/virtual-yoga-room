from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.blog_details, name='blog_details'),
    path('<int:blog_id>/add/', views.add_comment, name='add_comment'),
    path('update/<int:comment_id>/',
         views.update_comment, name='update_comment'),
    path('delete/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
]
