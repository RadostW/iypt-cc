# Generated by Django 2.0.3 on 2018-03-28 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0034_auto_20180328_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendeeproperty',
            old_name='optional',
            new_name='optional_tmp',
        ),
        migrations.RenameField(
            model_name='attendeeproperty',
            old_name='required',
            new_name='required_tmp',
        ),
    ]