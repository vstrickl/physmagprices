# Generated by Django 5.1.5 on 2025-01-15 06:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0003_remove_uploadfile_cloudinary_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
