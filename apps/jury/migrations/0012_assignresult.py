# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-05 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0001_initial'),
        ('tournament', '0016_auto_20170105_1843'),
        ('jury', '0011_auto_20161206_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_celery_results.TaskResult')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament')),
            ],
        ),
    ]