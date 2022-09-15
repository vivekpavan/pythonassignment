from rest_framework import viewsets
from .serializers import apiSerializer
from .models import apiModel

class apiViewSet(viewsets.ModelViewSet):
    queryset = apiModel.objects.all()
    serializer_class = apiSerializer
