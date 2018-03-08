# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0011_remove_peminjamankendaraan_supir'),
    ]

    operations = [
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='biaya_bbm',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='biaya_parkir',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='biaya_penginapan',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='biaya_perawatan',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='biaya_supir',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjamankendaraan',
            name='biaya_tol',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]