# Generated by Django 5.1.5 on 2025-01-15 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadedFile',
            new_name='UploadFile',
        ),
    ]
