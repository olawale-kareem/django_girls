from rest_framework import viewsets

from .serializers import GeeksSerializer
from .models import GeeksModel

# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
	# define queryset
    # get all  the instance of the GeeksModel
	queryset = GeeksModel.objects.all()

	# specify serializer to be used
	serializer_class = GeeksSerializer

