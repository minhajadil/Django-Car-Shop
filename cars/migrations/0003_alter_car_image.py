# Generated by Django 5.0 on 2024-01-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_card_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='cars/media/uploads/'),
        ),
    ]