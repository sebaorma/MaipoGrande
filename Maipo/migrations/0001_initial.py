# Generated by Django 3.1.7 on 2021-07-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=50)),
                ('solicitante', models.CharField(max_length=100)),
                ('produtco', models.CharField(max_length=100)),
                ('cantidad', models.FloatField()),
                ('categoria', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'solicitud',
                'verbose_name_plural': 'solicitudes',
            },
        ),
    ]
