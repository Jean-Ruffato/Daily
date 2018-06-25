# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    # user = models.OneToOneField(User, related_name='profile')
    nome = models.CharField('nome', max_length=30)

    def __str__(self):
        return self.nome


class Projetos(models.Model):
    ID = models.AutoField('ID', primary_key=True)
    Projeto = models.CharField('Projeto', max_length=50)
    Responsavel = models.CharField('Responsavel', max_length=50)
    Integrantes = models.CharField('Integrantes', max_length=1000, null=True)
    Prazo = models.DateField('Prazo', blank=True, null=True)
    Horas = models.IntegerField('Horas', blank=True, null=True, default='01')
    Valor = models.IntegerField('Valor', blank=True, null=True, default='01')
    Status = models.CharField('Status', max_length=20, default='Pendente')
    Descricao = models.TextField('Descricao', max_length=500)

    def __str__(self):
        return self.Projeto

    class Meta:
        permissions = (
            ("Coordenador", "Coordenador"),
            ("Funcionario", "Funcionario"),
            ("RH", "RH"),
            ("Financeiro", "Financeiro"),
            ("Gerente", "Gerente"),
            ("Diretor", "Diretor"),
            ("Administrador", "Administrador"),
        )
        db_table = 'Projetos'
        verbose_name = 'Projetos'
        verbose_name_plural = 'Projetos'


class Atividades(models.Model):
    ID = models.AutoField('ID', primary_key=True)
    Nome = models.CharField('Nome', max_length=50)
    Inicio = models.DateTimeField('Inicial', blank=True, null=True)
    Fim = models.DateTimeField('Final', blank=True, null=True)
    Projeto = models.CharField('Projeto', max_length=40)
    Atividade = models.CharField('Atividade', max_length=40)
    Prazo = models.DateField('Prazo', blank=True, null=True)
    Status = models.CharField('Status', max_length=10, default='Pendente')
    Prioridade = models.IntegerField('prioridade', null=False, default=5)
    Descricao = models.TextField('Descricao', max_length=200)
    Horas = models.TimeField('Horas', blank=True, null=True, default='00:00:00')

    def __str__(self):
        return self.Nome

    class Meta:
        permissions = (
            ("Coordenador", "Coordenador"),
            ("Funcionario", "Funcionario"),
            ("RH", "RH"),
            ("Financeiro", "Financeiro"),
            ("Gerente", "Gerente"),
            ("Diretor", "Diretor"),
            ("Administrador", "Administrador"),
        )
        db_table = 'Atividades'
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

