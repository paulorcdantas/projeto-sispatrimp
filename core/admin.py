# core/admin.py

from django.contrib import admin
from .models import (
    Polo, 
    Cidade, 
    Local,
    TipoEquipamento,
    FabricanteEquipamento,
    Equipamento,
    Movimentacao
)

# Registando todos os modelos aqui
admin.site.register(Polo)
admin.site.register(Cidade)
admin.site.register(Local)
admin.site.register(TipoEquipamento)
admin.site.register(FabricanteEquipamento)
admin.site.register(Equipamento)
admin.site.register(Movimentacao)