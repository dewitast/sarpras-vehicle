# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-29 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0019_peminjamankendaraan_status_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='email_peminjam',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]