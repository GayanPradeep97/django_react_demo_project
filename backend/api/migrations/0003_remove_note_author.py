# Generated by Django 5.0.7 on 2024-08-06 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_auther_note_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='author',
        ),
    ]
