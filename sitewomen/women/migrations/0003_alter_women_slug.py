# Generated by Django 5.1.1 on 2024-10-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
