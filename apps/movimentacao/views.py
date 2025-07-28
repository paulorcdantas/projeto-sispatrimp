# apps/movimentacao/views.py

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from core.models import Movimentacao
from .serializers import MovimentacaoSerializer

class MovimentacaoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar movimentações.
    """
    queryset = Movimentacao.objects.all().order_by('-data_movimentacao')
    serializer_class = MovimentacaoSerializer
    permission_classes = [DjangoModelPermissions] # Garante que as permissões do Django são verificadas