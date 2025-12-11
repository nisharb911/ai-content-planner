# planner/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_list_create, name='posts_list_create'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('external/', views.fetch_external_data, name='external_data'),
]
