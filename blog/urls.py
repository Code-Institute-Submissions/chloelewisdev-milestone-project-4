from django.urls import path
from . import views

urlpatterns = [
     path('', views.blog, name='blog'),
     path('add/', views.new_blog, name='new_blog'),
     path('edit/<int:blog_id>/', views.edit_blog,
          name='edit_blog'),
     path('delete/<int:blog_id>/', views.delete_blog,
     name='delete_blog'),
]