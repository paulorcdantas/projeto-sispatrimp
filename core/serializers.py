# core/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adiciona os nomes dos grupos do utilizador ao payload do token
        token['groups'] = [group.name for group in user.groups.all()]
        return token

class UserDetailsSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'groups')
    def get_groups(self, user):
        return [group.name for group in user.groups.all()]