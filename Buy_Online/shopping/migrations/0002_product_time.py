# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
