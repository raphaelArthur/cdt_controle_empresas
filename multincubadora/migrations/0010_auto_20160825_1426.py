# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-25 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multincubadora', '0009_auto_20160819_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colaborador_multi',
            options={'ordering': ['nome']},
        ),
    ]
