# Generated by Django 4.2.9 on 2024-02-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clasificados', '0003_anuncio_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='precio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]