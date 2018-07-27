# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-29 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0025_auto_20180125_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': (('manage_team', 'Manage the Team where user is TL'), ('manage_data', 'Set users participation data'), ('accept_team', 'Accept new Teams'), ('accept_role', 'Accept new Persons for Role'), ('accept_juror', 'Accept new Jurors'), ('manage_all_teams', 'Manage all Teams'), ('view_all_data', 'View all Attendee Data'))},
        ),
    ]