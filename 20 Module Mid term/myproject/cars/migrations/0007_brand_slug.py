# Generated by Django 5.0.4 on 2024-05-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_remove_brand_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
