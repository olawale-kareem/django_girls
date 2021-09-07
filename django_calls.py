

from django.contrib.auth.models import User  # this brings the superuser down
User.objects.get(username='mark')            # This queries the superuser for the name mark
# Post.objects.filter(title__contains='title') # a filter query to get title feilds that contain the word title
# Post.objects.filter(published_date__lte=timezone.now()) #get already published news
# Post.objects.order_by('published_date')  #order by published date
# Post.objects.order_by('-published_date') # reverse the ordering
# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  #get articles with past published date and order by the published date
# Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #reverse the order


# authentication  and authorisation tool in django 
# from django.contrib.auth.decorators import login_required         # to protect your views
# from django.contrib.auth.views import LoginView, LogoutView       # to register your view in settings.py



# heroku : more settings
# $ heroku ps:scale web=1
# $ heroku open
# $ heroku run python manage.py migrate
# $ heroku run python manage.py createsuperuser


# This is an optional setting on the wsgi.py file, it didn't
# # from whitenoise.django import DjangoWhiteNoise
# application = DjangoWhiteNoise(application)

# to configure postgress for heroku
# register your secrets on heroku if you use python decouple
# you need to add this line of code to your settings.py file
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)


# django restful- api
# Steps to creating a restful api
# install this 3 dependencies as so, pip install djangorestframework markdown django-filter
# Add 'rest_framework' to INSTALLED_APPS
# Create a app and model
# Serialization
# Creating a viewset
# Define URLs of API
# Run server and check API


# Micro Services
# A microservice is a small, loosely coupled distributed service. Microservice Architectures evolved as a solution to the scalability and innovation challenges with Monolith architectures (Monolith applications are typically huge – more 100, 000 line of code). It allows you to take a large application and decompose or break into easily manageable small components with narrowly defined responsibilities.

# Reasons for using Microservice:
# In monolith application, there are few challenges:

# For a large application, it is difficult to understand the complexity and make code changes fast and correctly, sometimes it becomes hard to manage the code.
# Applications need extensive manual testing to ensure the impact of changes.
# For small change, the whole application needs to be built and deployed.
# The heavy application slows down start-up time.
# Benefits of Microservices:

# Small Modules –
# Application is broken into smaller modules which are easy for developers to code and maintain.
# Easier Process Adaption –
# By using microservices, new Technology & Process Adaption becomes easier. You can try new technologies with the newer microservices that we use.
# Independent scaling –
# Each microservice can scale independently via X-axis scaling (cloning with more CPU or memory) and Z-axis scaling (sharding), based upon their needs.
# Unaffected –
# Large applications remain largely unaffected by the failure of a single module.
# DURS –
# Each service can be independently DURS (deployed, updated, replaced, and scaled).
# Restrictions of Microservices:

# Configuration Management –
# As it becomes granular the headache comes for configuring the services and monitoring those. You need to maintain configurations for hundreds of components across environments.
# Debugging –
# Tracking down the service failure is painstaking job. You might need to look into multiple services across different components. Centralized Logging and Dashboards are essential to make it easy to debug problems.
# Automation – Because there are a number of smaller components instead of a monolith, you need to automate everything – Builds, Deployment, Monitoring etc.
# Testing –
# Needs a greater effort for end to end testing as it needs all the dependent services to be up and running.


# PaaS
# What is PaaS? Platform as a Service definition
# Platform as a service (PaaS) is a cloud computing model where a third-party provider delivers hardware and software tools to users over the internet. Usually, these tools are needed for application development. A PaaS provider hosts the hardware and software on its own infrastructure. As a result, 
# PaaS frees developers from having to install in-house hardware and software to develop or run a new application.
# What are the differences between PaaS, IaaS and SaaS?
# PaaS is one of three main categories of cloud computing services. The other two are software as a service (SaaS) and infrastructure as a service (IaaS).
# With IaaS, a provider supplies the basic compute, storage and networking infrastructure along with the hypervisor -- the virtualization layer. Users must then create virtual machines, install operating systems, support applications and data, and handle all of the configuration and management associated with those tasks. Examples of IaaS services are DigitalOcean, AWS and Google Compute Engine (GCE).
# With PaaS, a provider offers more of the application stack than IaaS solutions, adding operating systems, middleware (such as databases) and other runtimes into the cloud environment. PaaS products include AWS Elastic Beanstalk and Google App Engine.
# With SaaS, a provider offers an entire application stack. Users simply log in and use the application that runs completely on the provider's infrastructure. Typically, SaaS applications are completely accessible via internet web browser. SaaS providers manage all IT resources. Examples of SaaS include Salesforce, Dropbox and Google Workspace.
# examples of  PaaS 1.AWS Elastic Beanstalk. 2. Windows Azure.  3.Heroku



# todos
# automatic deploy on heroku ...done
# finnish github deploy  .. on hold
# finnish advance git   .. done
# check read up on Ai/machine learning ..done
# visit expresso to resubmit ... done
# sunday algorithms strictly ... skipped
# Ai course by deep learning on coursera.. look into that later. done


# finnish docker
# micro services with kubernatttes



