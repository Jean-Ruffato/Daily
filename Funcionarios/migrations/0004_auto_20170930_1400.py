# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-30 17:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionarios', '0003_remove_profile_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Perfil',
        ),
    ]
