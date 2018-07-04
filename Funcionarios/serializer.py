from rest_framework import serializers
from .models import Projetos, Atividades, Perfil


class ProjetosSerializer (serializers.ModelSerializer):
    """
        Classe para serialização de dados do modelo Projeto e servir uma Api com esses dados
    """
    class Meta:
        model = Projetos
        depth = 1
        fields = ['ID', 'Projeto', 'Responsavel', 'Integrantes',
                  'Prazo', 'Horas', 'Valor', 'Status', 'Descricao']


class AtividadesSerializer (serializers.ModelSerializer):
    """
        Classe para serialização de dados do modelo Atividades e servir uma Api com esses dados
    """
    class Meta:
        model = Atividades
        depth = 1
        fields = ['ID', 'Nome', 'Inicio', 'Fim', 'Projeto', 'Atividade',
                  'Prazo', 'Status', 'Prioridade', 'Descricao', 'Horas']


class PerfilSerializer (serializers.ModelSerializer):
    """
        Classe para serialização de dados do modelo Perfil e servir uma Api com esses dados
    """
    class Meta:
        model = Perfil
        depth = 1
        fields = ['nome']
