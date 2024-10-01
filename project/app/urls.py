from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_dets, name='blog_details'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blogs/<int:pk>/edit', views.update_blog, name='update_blog'),
    path('blogs/<int:pk>/delete', views.delete_blog, name='delete_blog')
]
