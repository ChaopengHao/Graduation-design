# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170511_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jdbookitem',
            name='channel',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='jdbookitem',
            name='img',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='jdbookitem',
            name='keywords',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='jdbookitem',
            name='price',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='jdbookitem',
            name='sub_tag',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='jdbookitem',
            name='tag',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='jdbookitem',
            name='title',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='jdbookitem',
            name='url',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='jdbookitem',
            name='value',
            field=models.CharField(max_length=125),
        ),
    ]
