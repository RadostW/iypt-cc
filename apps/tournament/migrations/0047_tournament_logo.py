# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-21 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0046_auto_20180320_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]