# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-01 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionarios', '0009_auto_20170930_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividades',
            name='Horas',
            field=models.TimeField(blank=True, null=True, verbose_name='Horas'),
        ),
    ]
