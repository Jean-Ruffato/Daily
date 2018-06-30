# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import re
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.db import connection
from django.shortcuts import render, redirect
from Funcionarios.models import Projetos, Atividades, Perfil
from .forms import CadastrarProjeto, DefinirAtividade, EditarProjeto, EditarAtividades, SignUpForm, EditarUsuarios, \
    Integrantes


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            nome = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
            nome_perfil = Perfil.objects.create(nome=nome)
            nome_perfil.save()
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'Coordenador/cadastrar_usuario.html', {'form': form})


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        projetos = Projetos.objects.filter(Responsavel=nome).order_by('Status')
        paginas = request.GET.get('paginas', 1)
        paginador = Paginator(projetos, 5)
        try:
            pag_proj = paginador.page(paginas)
        except PageNotAnInteger:
            pag_proj = paginador.page(1)
        except EmptyPage:
            pag_proj = paginador.page(paginador.num_pages)
        tarefas = Atividades.objects.filter(Nome=nome).order_by('Status').exclude(Status='Parado').exclude(
            Status='Finalizado')
        page = request.GET.get('page', 1)
        paginator = Paginator(tarefas, 5)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        lista_projetos = Projetos.objects.all()

        ano = date.today()

        janeiro = Atividades.objects.filter(Inicio__month='01', Inicio__year=ano.year, Status='Parado')
        contagem_janeiro = len(janeiro)

        fevereiro = Atividades.objects.filter(Inicio__month='02', Inicio__year=ano.year, Status='Parado')
        contagem_fevereiro = len(fevereiro)

        marco = Atividades.objects.filter(Inicio__month='03', Inicio__year=ano.year, Status='Parado')
        contagem_marco = len(marco)

        abril = Atividades.objects.filter(Inicio__month='04', Inicio__year=ano.year, Status='Parado')
        contagem_abril = len(abril)

        maio = Atividades.objects.filter(Inicio__month='05', Inicio__year=ano.year, Status='Parado')
        contagem_maio = len(maio)

        junho = Atividades.objects.filter(Inicio__month='06', Inicio__year=ano.year, Status='Parado')
        contagem_junho = len(junho)

        julho = Atividades.objects.filter(Inicio__month='07', Inicio__year=ano.year, Status='Parado')
        contagem_julho = len(julho)

        agosto = Atividades.objects.filter(Inicio__month='08', Inicio__year=ano.year, Status='Parado')
        contagem_agosto = len(agosto)

        setembro = Atividades.objects.filter(Inicio__month='09', Inicio__year=ano.year, Status='Parado')
        contagem_setembro = len(setembro)

        outubro = Atividades.objects.filter(Inicio__month='10', Inicio__year=ano.year, Status='Parado')
        contagem_outubro = len(outubro)

        novembro = Atividades.objects.filter(Inicio__month='11', Inicio__year=ano.year, Status='Parado')
        contagem_novembro = len(novembro)

        dezembro = Atividades.objects.filter(Inicio__month='12', Inicio__year=ano.year, Status='Parado')
        contagem_dezembro = len(dezembro)
        return render(request, 'Coordenador/home.html',
                      {'Projetos': projetos, 'Tarefas': tarefas, 'usuario': nome, 'users': users,
                       'Paginacao_Projetos': pag_proj, 'Projeto': lista_projetos,
                       'janeiro': contagem_janeiro, 'fevereiro': contagem_fevereiro, 'marco': contagem_marco,
                       'abril': contagem_abril, 'maio': contagem_maio,
                       'junho': contagem_junho, 'julho': contagem_julho, 'agosto': contagem_agosto,
                       'setembro': contagem_setembro, 'outubro': contagem_outubro,
                       'novembro': contagem_novembro, 'dezembro': contagem_dezembro})


def usuarios(request):
    usuario = User.objects.all()
    return render(request, 'Coordenador/usuarios.html', {'usuario': usuario})


def editar_usuarios(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        ident = User.objects.get(id=pk)
        form = EditarUsuarios(request.POST or None, instance=ident)
        if form.is_valid():
            form.save()
            return redirect('Coordenador:home')
        else:
            return render(request, 'Coordenador/editar_usuarios.html', {'editar_usuarios': form})


def definir_atividade(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        form = DefinirAtividade(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Coordenador:home')
        else:
            return render(request, 'Coordenador/definir_atividade.html', {'definir_atividade': form})


def editar_projeto(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        ident = Projetos.objects.get(ID=pk)
        form = EditarProjeto(request.POST or None, instance=ident)
        if form.is_valid():
            form.save()
            return redirect('Coordenador:home')
        else:
            return render(request, 'Coordenador/editar_projeto.html', {'editar_projeto': form})


# View para renderizar a página de projetos, converter para lista e executar o post do formulário.
def integrantes(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        ident = Projetos.objects.get(ID=pk)
        form = Integrantes(request.POST or None, instance=ident)
        if form.is_valid():
            integrantes_banco = Projetos.objects.get(ID=pk)
            lista_integrantes = [integrantes_banco.Integrantes] + [form.cleaned_data.get('Integrantes')]
            rm_string1 = re.sub(r'Perfil', '', str(lista_integrantes))
            rm_string2 = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ, ]', '', str(rm_string1))
            Projetos.objects.filter(ID=pk).update(Integrantes=rm_string2)
            return redirect('Coordenador:perfil_projetos')
        else:
            return render(request, 'Coordenador/integrantes.html', {'integrantes': form})


def editar_atividade(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        ident = Atividades.objects.get(ID=pk)
        form = EditarAtividades(request.POST or None, instance=ident)
        if form.is_valid():
            form.save()
            return redirect('Coordenador:home')
        else:
            return render(request, 'Coordenador/editar_atividades.html', {'editar_atividades': form})


def cadastrar_projeto(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        form = CadastrarProjeto(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Coordenador:definir_atividade')
        else:
            return render(request, 'Coordenador/cadastrar_projeto.html', {'cadastrar_projeto': form})


def perfil_projetos(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        perfil = Projetos.objects.filter().order_by('Status')
        page = request.GET.get('page', 1)
        paginator = Paginator(perfil, 5)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'Coordenador/perfil_projetos.html', {'perfil': perfil,
                                                                    'users': users})


def perfil_projeto(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        user = User.objects.get(pk=request.user.id)
        nome = user.first_name + ' ' + user.last_name
        perfil = Projetos.objects.get(ID=pk)
        projeto = perfil.Projeto
        cursor = connection.cursor()
        cursor.execute('''SELECT SUM("Atividades"."Horas"::time) FROM "Atividades" WHERE "Atividades"."Projeto" = '%s' ''' % projeto)
        horas = cursor.fetchone()
        horas_str = str(horas[0])
        horas_convertidas = datetime.strptime(horas_str, '%H:%M:%S')
        horas_executadas = horas_convertidas.hour
        calculo_progresso = (horas_executadas / perfil.Horas) * 100
        progresso = int(calculo_progresso)
        atividades = Atividades.objects.filter(Nome=nome, Status='Pendente')
        return render(request, 'Coordenador/perfil_projeto.html', {'perfil': perfil, 'usuario': nome,
                                                                   'atividades': atividades, 'horas_executadas': horas_executadas, 'progresso': progresso})


def apagar_projeto(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/?next=%s' % request.path)
    else:
        projetos = Projetos.objects.filter(ID=pk)
        projetos.delete()
        return render(request, 'Coordenador/apagar_projeto.html', {})
