# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-07 23:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20180101_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': (('manage_team', 'Manage the Team where user is TL'), ('manage_data', 'Set users participation data'), ('accept_team', 'Accept new Teams'))},
        ),
    ]