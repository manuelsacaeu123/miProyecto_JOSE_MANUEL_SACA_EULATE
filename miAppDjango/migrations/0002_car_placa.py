# Generated by Django 3.2.9 on 2021-11-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAppDjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='placa',
            field=models.IntegerField(default=0),
        ),
    ]
