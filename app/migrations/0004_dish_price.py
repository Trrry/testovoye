# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170928_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='price',
            field=models.CharField(help_text='Dish price', max_length=10, null=True),
        ),
    ]