# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pctec', '0004_auto_20160720_1927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Funcionario',
            new_name='Colaborador',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='funcionarios',
            new_name='Colaboradores',
        ),
    ]
