# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Funcionarios.models import Atividades, Projetos, Perfil
from .serializer import ProjetosSerializer, AtividadesSerializer, PerfilSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProjetosListView(APIView):
    serializer_class = ProjetosSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Projetos.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "403 Forbidden"}, status=status.HTTP_409_CONFLICT)


class ProjetosIDView(APIView):
    serializer_class = ProjetosSerializer

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(Projetos.objects.get(pk=pk))
        return Response(serializer.data)


class AtividadesListView(APIView):
    serializer_class = AtividadesSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Atividades.objects.all(), many=True)
        return Response(serializer.data)


class AtividadesIDView(APIView):
    serializer_class = AtividadesSerializer

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(Atividades.objects.get(pk=pk))
        return Response(serializer.data)


class PerfilListView(APIView):
    serializer_class = PerfilSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Perfil.objects.all(), many=True)
        return Response(serializer.data)


def iniciar(request, pk):
    """
        View para preencher os dados da tabela de funcionarios e tarefas.
        Também possúi queries para iniciar, pausar e parar uma atividade.
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        Atividades.objects.filter(Status='Executando').update(Fim=datetime.now(), Status='Pendente')
        Atividades.objects.filter(ID=pk).update(Inicio=datetime.now(), Status='Executando')
        return render(request, 'Funcionarios/iniciar.html', {})


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        lista_atividades = Atividades.objects.all()
        return render(request, 'Funcionarios/home.html', {'lista_atividades': lista_atividades})


def continuar(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        """
            View para preencher os dados da tabela de funcionarios e tarefas.
            Também possúi queries para iniciar, pausar e parar uma atividade.
        """
        filtro_id = Atividades.objects.filter(ID=pk)
        executando = Atividades.objects.filter(Status='Executando').update(Fim=datetime.now(), Status='Parado')
        atividade = Atividades.objects.filter(Status='Parado')
        for filtrado in filtro_id:
            criar = Atividades.objects.create(Nome=nome, Inicio=datetime.now(), Projeto=filtrado.Projeto,
                                              Atividade=filtrado.Atividade, Descricao=filtrado.Descricao,
                                              Status='Executando')
            criar.save()
            padrao = '%Y-%m-%d %H:%M:%S'
            inicio = str(filtrado.Inicio)
            new_inicio = inicio[:19]
            fim = str(filtrado.Fim)
            new_fim = fim[:19]
            tempo_sessao = (datetime.strptime(new_fim, padrao) - datetime.strptime(new_inicio, padrao)).total_seconds()
            tempo = int(tempo_sessao)
            horas = tempo // 3600
            segs_restantes = tempo % 3600
            minutos = segs_restantes // 60
            segs_restantes_final = segs_restantes % 60
            horas_final = str(horas) + ':' + str(minutos) + ':' + str(segs_restantes_final)
            usuario = Atividades.objects.filter(ID=pk).update(Status='Parado', Horas=horas_final)
        return render(request, 'Funcionarios/continuar.html', {'Continuar': usuario})


def pausar(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        """
            View para preencher os dados da tabela de funcionarios e tarefas.
            Também possúi queries para iniciar, pausar e parar uma atividade.
        """
        usuario = Atividades.objects.filter(ID=pk).update(Fim=datetime.now(), Status='Pausado')
        atividade = Atividades.objects.filter(ID=pk)
        for atividades in atividade:
            padrao = '%Y-%m-%d %H:%M:%S'
            inicio = str(atividades.Inicio)
            new_inicio = inicio[:19]
            fim = str(atividades.Fim)
            new_fim = fim[:19]
            tempo_sessao = (datetime.strptime(new_fim, padrao) - datetime.strptime(new_inicio, padrao)).total_seconds()
            tempo = int(tempo_sessao)
            horas = tempo // 3600
            segs_restantes = tempo % 3600
            minutos = segs_restantes // 60
            segs_restantes_final = segs_restantes % 60
            horas_final = str(horas) + ':' + str(minutos) + ':' + str(segs_restantes_final)
            Atividades.objects.filter(ID=pk).update(Horas=horas_final)
            return render(request, 'Funcionarios/pausar.html', {'Pausar': usuario})


def parar(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        """
             View para preencher os dados da tabela de funcionarios e tarefas.
             Também possúi queries para iniciar, pausar e parar uma atividade.
        """
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        filtro_id = Atividades.objects.filter(ID=pk)
        for filtrado in filtro_id:
            criar = Atividades.objects.create(Nome=nome, Projeto=filtrado.Projeto,
                                              Atividade=filtrado.Atividade, Descricao=filtrado.Descricao, Status='Pendente')
            criar.save()
            Atividades.objects.filter(Status='pausado')
            if filtrado.Status == 'Pausado':
                Atividades.objects.filter(ID=pk).update(Status='Parado')
            else:
                Atividades.objects.filter(ID=pk).update(Fim=datetime.now(), Status='Parado')
                tempo = Atividades.objects.get(ID=pk)
                padrao = '%Y-%m-%d %H:%M:%S'
                inicio = str(tempo.Inicio)
                new_inicio = inicio[:19]
                fim = str(tempo.Fim)
                new_fim = fim[:19]
                tempo_sessao = (datetime.strptime(new_fim, padrao) - datetime.strptime(new_inicio, padrao)).total_seconds()
                tempo = int(tempo_sessao)
                horas = tempo // 3600
                segs_restantes = tempo % 3600
                minutos = segs_restantes // 60
                segs_restantes_final = segs_restantes % 60
                horas_final = str(horas) + ':' + str(minutos) + ':' + str(segs_restantes_final)
                Atividades.objects.filter(ID=pk).update(Horas=horas_final)
        return render(request, 'Funcionarios/parar.html', {})


def finalizar(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        """
            View para preencher os dados da tabela de funcionarios e tarefas.
            Também possúi queries para iniciar, pausar e parar uma atividade.
        """
        usuario = Atividades.objects.filter(ID=pk)
        usuario.delete()
        return render(request, 'Funcionarios/finalizar.html', {'Finalizar': usuario})


def funcionarios(request):
    """
        View para preencher os dados da tabela de funcionarios e tarefas.
        Também possúi queries para iniciar, pausar e parar uma atividade.
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        tarefas = Atividades.objects.filter(Nome=nome).order_by('Status').exclude(Status='Parado').exclude(Status='Finalizado')
        atividades_executadas = Atividades.objects.filter(Nome=nome, Status='Parado')
        atividades_pendentes = Atividades.objects.filter(Nome=nome, Status='Pendente')
        executadas = len(atividades_executadas)
        at_pendente = len(atividades_pendentes)
        page = request.GET.get('page', 1)
        paginator = Paginator(tarefas, 5)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'Funcionarios/funcionarios.html', {'Tarefas': tarefas, 'users': users, 'Executadas': executadas,
                                                                  'Pendentes': at_pendente})


def login(request):
    return render(request, 'Funcionarios/login.html', {})


def atividades(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        lista_atividades = Atividades.objects.filter(Nome=nome).exclude(Status='Pendente').order_by('Status')
        page = request.GET.get('page', 1)
        paginator = Paginator(lista_atividades, 10)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'Funcionarios/atividades.html', {'Lista_Atividades': lista_atividades,
                                                                'users': users})


def atividade(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        atividade = Atividades.objects.get(ID=pk)
        return render(request, 'Funcionarios/atividade.html', {'atividade': atividade, 'Nome': nome})


def pendentes(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name

        lista_atividades = Atividades.objects.filter(Nome=nome, Status='Pendente').order_by('Status')
        page = request.GET.get('page', 1)
        paginator = Paginator(lista_atividades, 5)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'Funcionarios/pendentes.html', {'Lista_Atividades': lista_atividades,
                                                               'users': users})


def pendente(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        atividade = Atividades.objects.get(ID=pk)
        return render(request, 'Funcionarios/pendente.html', {'atividade': atividade, 'Nome': nome})


def apagar(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        atividade = Atividades.objects.filter(ID=pk)
        atividade.delete()
        return render(request, 'Funcionarios/apagar.html', {})


def apagar_pendente(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        atividade = Atividades.objects.filter(ID=pk)
        atividade.delete()
        return render(request, 'Funcionarios/apagar_pendente.html', {})
