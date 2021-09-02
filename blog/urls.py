from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    
    path('posts/', post_list, name = 'post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<pk>/publish/', post_publish, name='post_publish'),
    path('post/<pk>/remove/', post_remove, name='post_remove'),

    path('post/new/', post_new, name='post_new'),
    path('drafts/', post_draft_list, name='post_draft_list'),
]


