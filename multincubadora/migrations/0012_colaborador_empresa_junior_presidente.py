# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-25 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multincubadora', '0011_colaborador_empresa_junior'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador_empresa_junior',
            name='presidente',
            field=models.BooleanField(default=False),
        ),
    ]