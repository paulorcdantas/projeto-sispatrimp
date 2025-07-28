from rest_framework import serializers
from core.models import Polo, Cidade, Local

class PoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polo
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    cidade_nome = serializers.CharField(source='cidade.nome_cidade', read_only=True)
    class Meta:
        model = Local
        fields = ['id', 'nome_local', 'cidade', 'cidade_nome']