# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pctec', '0014_auto_20160815_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='foto',
            field=models.ImageField(blank=True, default='/pctec/static/pctec/no_foto.png', null=True, upload_to='colaboradores/'),
        ),
    ]
