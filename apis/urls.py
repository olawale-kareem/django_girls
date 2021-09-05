from django.urls import include, path
from rest_framework import routers


from .views import *


router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'geeks', GeeksViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]
