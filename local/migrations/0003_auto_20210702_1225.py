# Generated by Django 3.1.7 on 2021-07-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0002_auto_20210702_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(to='local.Calidad'),
        ),
    ]
