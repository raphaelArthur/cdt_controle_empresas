# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-30 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pctec', '0015_auto_20160816_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='cracha',
            field=models.BooleanField(default=False, verbose_name='Possui Cracha?'),
        ),
    ]
