from django.contrib import admin
from .models import Post, Comment

my_models = [Post, Comment]
for model in my_models:
    admin.site.register(model)


