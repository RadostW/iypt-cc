# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0005_tournament_final_fight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='final_fight',
        ),
    ]