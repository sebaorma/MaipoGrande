# Generated by Django 3.1.7 on 2021-07-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0002_puja'),
    ]

    operations = [
        migrations.AddField(
            model_name='puja',
            name='producto',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
