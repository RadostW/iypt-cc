# Generated by Django 2.0.3 on 2018-04-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_payment_ref_attendee'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]