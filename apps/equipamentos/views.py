# apps/equipamentos/views.py

from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions # <-- IMPORTAÇÃO ADICIONADA
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from core.models import Equipamento, TipoEquipamento, FabricanteEquipamento, Local, Movimentacao
from .serializers import EquipamentoSerializer, TipoEquipamentoSerializer, FabricanteEquipamentoSerializer
from apps.movimentacao.serializers import MovimentacaoSerializer
from core.models import Equipamento, TipoEquipamento, FabricanteEquipamento

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all().order_by('nome_equipamento')
    serializer_class = EquipamentoSerializer
    permission_classes = [DjangoModelPermissions] # <-- LINHA ADICIONADA
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['patrimonio', 'local__nome_local']
    filterset_fields = ['tipo', 'status', 'local']

class TipoEquipamentoViewSet(viewsets.ModelViewSet):
    queryset = TipoEquipamento.objects.all()
    serializer_class = TipoEquipamentoSerializer
    permission_classes = [DjangoModelPermissions] # <-- LINHA ADICIONADA
    pagination_class = None

class FabricanteEquipamentoViewSet(viewsets.ModelViewSet):
    queryset = FabricanteEquipamento.objects.all()
    serializer_class = FabricanteEquipamentoSerializer
    permission_classes = [DjangoModelPermissions] # <-- LINHA ADICIONADA
    pagination_class = None

class DashboardStatsView(APIView):
    # A view do dashboard não precisa de permissões de modelo,
    # pois a permissão global IsAuthenticated já a protege.
    def get(self, request, format=None):
        total_equipamentos = Equipamento.objects.count()
        total_locais = Local.objects.count()
        total_movimentacoes = Movimentacao.objects.count()
        equipamentos_por_status = Equipamento.objects.values('status').annotate(total=Count('status')).order_by('-total')
        ultimas_movimentacoes = Movimentacao.objects.order_by('-data_movimentacao')[:5]
        ultimas_movimentacoes_serializer = MovimentacaoSerializer(ultimas_movimentacoes, many=True)
        data = {
            'total_equipamentos': total_equipamentos,
            'total_locais': total_locais,
            'total_movimentacoes': total_movimentacoes,
            'equipamentos_por_status': list(equipamentos_por_status),
            'ultimas_movimentacoes': ultimas_movimentacoes_serializer.data
        }
        return Response(data)