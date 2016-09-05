# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 19:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pctec', '0003_auto_20160720_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sala', models.CharField(max_length=50)),
                ('tel1', models.CharField(max_length=14, verbose_name='Telefone 1')),
                ('tel2', models.CharField(blank=True, max_length=14, verbose_name='Telefone 2')),
                ('tel3', models.CharField(blank=True, max_length=14, verbose_name='Telefone 3')),
                ('email', models.EmailField(max_length=254)),
                ('razao_social', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=14)),
                ('data_entrada_pctec', models.DateField(default=datetime.date.today, verbose_name='Data de Entrada no PCTec')),
                ('data_abertura', models.DateField(default=datetime.date.today, verbose_name='Data de Abertura')),
                ('descricao', models.TextField(blank=True)),
                ('observacao', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='funcionarios',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cep',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='endereco',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='rg',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='tel1',
            field=models.CharField(max_length=14, verbose_name='Telefone 1'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='tel2',
            field=models.CharField(blank=True, max_length=14, verbose_name='Telefone 2'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='tel3',
            field=models.CharField(blank=True, max_length=14, verbose_name='Telefone 3'),
        ),
        migrations.DeleteModel(
            name='Empresas',
        ),
        migrations.AddField(
            model_name='empresa',
            name='funcionarios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pctec.Funcionario'),
        ),
    ]
