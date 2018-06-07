# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from Funcionarios.models import Projetos, Atividades, Perfil
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Usuário *')
    first_name = forms.CharField(label='Nome *', max_length=30, required=True)
    last_name = forms.CharField(label='Sobrenome *', max_length=30, required=True)
    email = forms.EmailField(label='E-mail *', max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class CadastrarProjeto(forms.ModelForm):
    Responsavel = forms.ModelChoiceField(queryset=Perfil.objects.all())
    Prazo = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    Descricao = forms.CharField(label='Descrição', widget=forms.Textarea)

    class Meta:
        model = Projetos
        exclude = ['Status']


class DefinirAtividade(forms.ModelForm):
    Nome = forms.ModelChoiceField(queryset=Perfil.objects.all())
    Projeto = forms.ModelChoiceField(queryset=Projetos.objects.all())
    Atividade = forms.CharField()
    Prazo = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    Descricao = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Atividades
        exclude = ['Inicio', 'Fim', 'Horas', 'Status', 'Departamento']


class EditarUsuarios(ModelForm):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'date_joined', 'user_permissions']


class EditarProjeto(ModelForm):
    Responsavel = forms.ModelChoiceField(queryset=Perfil.objects.all())
    Projeto = forms.ModelChoiceField(queryset=Projetos.objects.all())
    Prazo = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    status = (
        ('Executando', 'Executando'),
        ('Pendente', 'Pendente'),
        ('Parado', 'Parado'),
        ('Finalizado', 'Finalizado'),
    )
    Status = forms.ChoiceField(choices=status)
    Descricao = forms.CharField(label='Descrição', widget=forms.Textarea)

    class Meta:
        model = Projetos
        exclude = ['']


class EditarAtividades(ModelForm):
    Nome = forms.ModelChoiceField(queryset=Perfil.objects.all())
    Projeto = forms.ModelChoiceField(queryset=Projetos.objects.all())
    status = (
        ('Executando', 'Executando'),
        ('Pendente', 'Pendente'),
        ('Parado', 'Parado'),
        ('Finalizado', 'Finalizado'),
    )
    Status = forms.ChoiceField(choices=status)
    Prazo = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Atividades
        exclude = ['Inicio', 'Fim', 'Horas']
