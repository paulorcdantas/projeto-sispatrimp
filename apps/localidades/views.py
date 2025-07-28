# apps/localidades/views.py

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from core.models import Polo, Cidade, Local
from .serializers import PoloSerializer, CidadeSerializer, LocalSerializer

class PoloViewSet(viewsets.ModelViewSet):
    queryset = Polo.objects.all().order_by('nome_polo')
    serializer_class = PoloSerializer
    permission_classes = [DjangoModelPermissions]
    pagination_class = None

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all().order_by('nome_cidade')
    serializer_class = CidadeSerializer
    permission_classes = [DjangoModelPermissions]
    pagination_class = None

# GARANTA QUE LocalViewSet NÃO TEM 'pagination_class = None'
# para que ele use a paginação global definida no settings.py
class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all().order_by('nome_local')
    serializer_class = LocalSerializer
    permission_classes = [DjangoModelPermissions]
    pagination_class = None
    
