# Generated by Django 5.0 on 2024-01-06 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_on',
        ),
    ]
