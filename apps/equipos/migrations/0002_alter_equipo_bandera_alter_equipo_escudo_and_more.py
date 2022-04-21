# Generated by Django 4.0.4 on 2022-04-21 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='bandera',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bandera del equipo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='escudo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Escudo del equipo'),
        ),
        migrations.AlterField(
            model_name='historicalequipo',
            name='bandera',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Bandera del equipo'),
        ),
        migrations.AlterField(
            model_name='historicalequipo',
            name='escudo',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Escudo del equipo'),
        ),
    ]