# apps/movimentacao/serializers.py

from rest_framework import serializers
from core.models import Movimentacao # Apenas o modelo de movimentacao

class MovimentacaoSerializer(serializers.ModelSerializer):
    # Nomes legíveis dos campos relacionados
    equipamento_nome = serializers.CharField(source='equipamento.nome_equipamento', read_only=True)
    local_origem_nome = serializers.CharField(source='local_origem.nome_local', read_only=True)
    local_destino_nome = serializers.CharField(source='local_destino.nome_local', read_only=True)
    # Supondo que seu modelo User tem um campo 'username'
    usuario_nome = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Movimentacao
        fields = [
            'id', 'equipamento', 'equipamento_nome', 'local_origem', 'local_origem_nome',
            'local_destino', 'local_destino_nome', 'data_movimentacao', 'observacao',
            'usuario', 'usuario_nome'
        ]