from rest_framework import serializers
from core.models import Equipamento, TipoEquipamento, FabricanteEquipamento

# Serializer para o modelo TipoEquipamento
class TipoEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEquipamento
        fields = '__all__'

# Serializer para o modelo FabricanteEquipamento
class FabricanteEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricanteEquipamento
        fields = '__all__'

# Serializer principal para o modelo Equipamento
class EquipamentoSerializer(serializers.ModelSerializer):
    # Campos 'read_only' para mostrar os nomes em vez dos IDs
    local_nome = serializers.CharField(source='local.nome_local', read_only=True, allow_null=True)
    tipo_nome = serializers.CharField(source='tipo.nome_tipo', read_only=True)
    fabricante_nome = serializers.CharField(source='fabricante.nome_fabricante', read_only=True)

    class Meta:
        model = Equipamento
        # Lista de todos os campos que a API irá expor
        fields = [
            'id',
            'nome_equipamento',
            'patrimonio',
            'mac_address',
            'local',
            'local_nome',
            'tipo',
            'tipo_nome',
            'fabricante',
            'fabricante_nome',
            'status'
        ]