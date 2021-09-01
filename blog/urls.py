from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('posts/', post_list, name = 'posts'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/new/', post_new, name='post_new'),
]


