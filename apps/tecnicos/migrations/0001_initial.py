# Generated by Django 4.0.4 on 2022-04-20 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=255, verbose_name='Rol')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCuerpo_Tecnico',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('nacionalidad', models.CharField(max_length=255, verbose_name='Nacionalidad')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('equipo', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='equipos.equipo')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('rol', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tecnicos.rol')),
            ],
            options={
                'verbose_name': 'historical Cuerpo Técnico',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Cuerpo_Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('nacionalidad', models.CharField(max_length=255, verbose_name='Nacionalidad')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.equipo')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecnicos.rol')),
            ],
            options={
                'verbose_name': 'Cuerpo Técnico',
                'verbose_name_plural': 'Cuerpo Técnico',
            },
        ),
    ]
