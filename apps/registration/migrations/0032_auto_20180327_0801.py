# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-27 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0031_attendeeproperty_apply_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('int', 'Integer'), ('string', 'String'), ('datetime', 'datetime'), ('date', 'date'), ('image', 'image'), ('pdf', 'pdf'), ('text', 'text'), ('gender', 'gender'), ('boolean', 'boolean'), ('boolean_true', 'required true boolean'), ('preferred_name', 'preferred name'), ('preferred_name_short', 'preferred name short'), ('choice', 'Select One'), ('multiple_choice', 'Select Multiple'), ('conflict_origins', 'Conflict with Origins'), ('country', 'Country (ISO)'), ('problem', 'Problem')], max_length=30),
        ),
    ]