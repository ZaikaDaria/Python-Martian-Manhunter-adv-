# Generated by Django 3.0 on 2021-08-11 15:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8-15}$')]),
        ),
    ]
