# Generated by Django 4.1.5 on 2023-01-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_craftsman_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craftsman',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]