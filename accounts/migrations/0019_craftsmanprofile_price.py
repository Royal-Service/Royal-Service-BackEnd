# Generated by Django 4.1.5 on 2023-01-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_craftsmanprofile_crafts_alter_user_crafts'),
    ]

    operations = [
        migrations.AddField(
            model_name='craftsmanprofile',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10),
        ),
    ]