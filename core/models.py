# core/models.py

from django.db import models
from django.contrib.auth.models import User

# Modelos de Localidades
class Polo(models.Model):
    nome_polo = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_polo

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    polo = models.ForeignKey(Polo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_cidade

class Local(models.Model):
    nome_local = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_local

# Modelos de Equipamentos
class TipoEquipamento(models.Model):
    nome_tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_tipo

class FabricanteEquipamento(models.Model):
    nome_fabricante = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_fabricante

class Equipamento(models.Model):
    nome_equipamento = models.CharField(max_length=150)
    patrimonio = models.CharField(max_length=50, unique=True, blank=True, null=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True, verbose_name="Endereço MAC")
    status = models.CharField(max_length=50, default='ATIVO')
    local = models.ForeignKey(Local, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.ForeignKey(TipoEquipamento, on_delete=models.PROTECT)
    fabricante = models.ForeignKey(FabricanteEquipamento, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome_equipamento

# Modelo de Movimentação
class Movimentacao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    local_origem = models.ForeignKey(Local, related_name='movimentacoes_origem', on_delete=models.SET_NULL, null=True, blank=True)
    local_destino = models.ForeignKey(Local, related_name='movimentacoes_destino', on_delete=models.CASCADE)
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.equipamento.nome_equipamento} - {self.data_movimentacao.strftime('%d/%m/%Y')}"