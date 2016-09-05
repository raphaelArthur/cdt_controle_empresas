# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pctec', '0007_auto_20160721_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='Colaboradores',
        ),
        migrations.AddField(
            model_name='empresa',
            name='Colaboradores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pctec.Colaborador'),
        ),
    ]
