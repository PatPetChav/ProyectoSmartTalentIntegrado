# Generated by Django 3.2 on 2022-06-14 03:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocatoria',
            name='convocatoria_photo',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]