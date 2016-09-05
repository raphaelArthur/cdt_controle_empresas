# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pctec', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresas',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='tel',
        ),
        migrations.AddField(
            model_name='empresas',
            name='tel1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='empresas',
            name='tel2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='empresas',
            name='tel3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='tel1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='tel2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='tel3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Telefone',
        ),
    ]
