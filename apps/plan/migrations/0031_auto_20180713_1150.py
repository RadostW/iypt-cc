# Generated by Django 2.0.3 on 2018-07-13 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_participationrole_attending'),
        ('plan', '0030_round_publish_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='fight',
            name='operators',
            field=models.ManyToManyField(blank=True, to='account.Attendee'),
        ),
        migrations.AlterField(
            model_name='fight',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='old_operator', to='account.Attendee'),
        ),
    ]