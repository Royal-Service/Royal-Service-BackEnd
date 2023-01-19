# Generated by Django 4.1.5 on 2023-01-19 10:20

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='day',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 PM', '12 PM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM')], default='3 PM', max_length=10),
        ),
    ]