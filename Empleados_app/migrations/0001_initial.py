# Generated by Django 5.1 on 2024-11-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id_empleado', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido_p', models.CharField(max_length=30)),
                ('apellido_m', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('matricula', models.CharField(max_length=20)),
                ('celular', models.PositiveIntegerField()),
                ('puesto', models.CharField(max_length=30)),
                ('salario', models.PositiveIntegerField()),
            ],
        ),
    ]
