# Generated by Django 2.0.3 on 2018-07-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jury', '0026_auto_20180623_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='juror',
            name='bias',
            field=models.FloatField(default=0),
        ),
    ]