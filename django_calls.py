

from django.contrib.auth.models import User  # this brings the superuser down
User.objects.get(username='mark')            # This queries the superuser for the name mark
# Post.objects.filter(title__contains='title') # a filter query to get title feilds that contain the word title
# Post.objects.filter(published_date__lte=timezone.now()) #get already published news
# Post.objects.order_by('published_date')  #order by published date
# Post.objects.order_by('-published_date') # reverse the ordering
# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  #get articles with past published date and order by the published date
# Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #reverse the order

# CSS : cascading style sheets

# from django.contrib.auth.decorators import login_required  #to protect your views


# heroku : more settings
# $ heroku ps:scale web=1
# $ heroku open
# $ heroku run python manage.py migrate
# $ heroku run python manage.py createsuperuser


# # from whitenoise.django import DjangoWhiteNoise
# application = DjangoWhiteNoise(application)


# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)



