# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pctec', '0012_auto_20160729_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='contato',
            field=models.BooleanField(default=False, verbose_name='Definir como Contato'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='empresa/'),
        ),
    ]
