from django.contrib import admin
from .models import Post

my_models = [Post]
for model in my_models:
    admin.site.register(model)


