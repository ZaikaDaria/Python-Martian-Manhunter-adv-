# Generated by Django 3.0 on 2021-08-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0002_dealer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
