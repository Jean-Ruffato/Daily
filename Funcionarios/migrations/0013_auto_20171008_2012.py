# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionarios', '0012_auto_20171008_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='Valor',
            field=models.IntegerField(blank=True, default='01', null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='projetos',
            name='Descricao',
            field=models.TextField(max_length=500, verbose_name='Descricao'),
        ),
    ]
