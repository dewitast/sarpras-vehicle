# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0013_auto_20180309_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilpeminjaman',
            name='supir',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='peminjaman.Supir'),
            preserve_default=False,
        ),
    ]
