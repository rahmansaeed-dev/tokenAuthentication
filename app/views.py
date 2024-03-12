from .models import Person
from  .serilizers import PersonModelSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ModelViewSetview(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]



