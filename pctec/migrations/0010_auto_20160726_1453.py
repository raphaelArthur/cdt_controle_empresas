# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 14:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pctec', '0009_auto_20160726_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AddField(
            model_name='empresa',
            name='data_abertura',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Abertura'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='entrada_pctec',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Entrada PCTec'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='razao_social',
            field=models.CharField(default='', max_length=200),
        ),
    ]
