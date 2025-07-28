# core/views.py

import json
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
# IMPORTAÇÃO CORRIGIDA: Importa os nomes corretos dos modelos
from .models import (
    Polo, 
    Cidade, 
    Local,
    TipoEquipamento,
    FabricanteEquipamento,
    Equipamento
)

class MyTokenObtainPairView(TokenObtainPairView):
    """
    Substitui a view de login padrão para usar o nosso serializer personalizado.
    """
    serializer_class = MyTokenObtainPairSerializer

def home(request):
    # Verifica se a ação de popular foi chamada pela URL
    if request.GET.get('action') == 'populate_db':
        
        # --- Popular Polos e Cidades ---
        # O seu ficheiro JSON chama-se 'regioes.json', mas ele contém Polos.
        polos_path = 'core/static/json/regioes.json' 
        with open(polos_path, 'r', encoding='utf-8') as file:
            polos_data = json.load(file)
            for nome_polo, cidades in polos_data.items():
                # LÓGICA CORRIGIDA: Usa o modelo 'Polo' e o campo 'nome_polo'
                polo_obj, _ = Polo.objects.get_or_create(nome_polo=nome_polo)
                for nome_cidade in cidades:
                    Cidade.objects.get_or_create(
                        nome_cidade=nome_cidade, 
                        polo=polo_obj
                    )

        # --- Popular Locais ---
        locais_path = 'core/static/json/locais.json'
        with open(locais_path, 'r', encoding='utf-8') as file:
            locais_data = json.load(file)
            for nome_cidade, locais in locais_data.items():
                cidade_obj = Cidade.objects.get(nome_cidade=nome_cidade)
                for local_info in locais:
                    # LÓGICA CORRIGIDA: Usa o campo 'nome_local' e remove 'descricao'
                    Local.objects.get_or_create(
                        nome_local=local_info['local'],
                        cidade=cidade_obj
                    )

        # --- Popular Equipamentos ---
        equipamentos_path = 'core/static/json/equipamentos.json'
        with open(equipamentos_path, 'r', encoding='utf-8') as file:
            equipamentos_data = json.load(file)
            for equipamento_data in equipamentos_data:
                # LÓGICA CORRIGIDA: Usa os campos 'nome_tipo' e 'nome_fabricante'
                tipo_obj, _ = TipoEquipamento.objects.get_or_create(nome_tipo=equipamento_data['tipo'])
                fabricante_obj, _ = FabricanteEquipamento.objects.get_or_create(nome_fabricante=equipamento_data['marca'])
                
                try:
                    local_obj = Local.objects.get(nome_local=equipamento_data['local'])
                except Local.DoesNotExist:
                    local_obj = None

                Equipamento.objects.get_or_create(
                    patrimonio=equipamento_data['patrimonio'],
                    defaults={
                        'nome_equipamento': f"Equipamento {equipamento_data['patrimonio']}",
                        'tipo': tipo_obj,
                        'fabricante': fabricante_obj,
                        'local': local_obj,
                    }
                )
        
        return HttpResponse("Banco de dados populado com sucesso!")

    return HttpResponse("Página inicial. Para popular o banco, adicione ?action=populate_db à URL.")