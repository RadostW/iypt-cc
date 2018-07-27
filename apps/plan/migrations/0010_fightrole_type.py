# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0009_auto_20161107_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='fightrole',
            name='type',
            field=models.CharField(blank=True, choices=[('rep', 'Reporter'), ('opp', 'Opponent'), ('rev', 'Reviewer'), ('obs', 'Observer')], max_length=3, null=True),
        ),
    ]