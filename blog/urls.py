from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('posts/', post_list, name = 'posts'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]


