# Generated by Django 4.0.1 on 2022-01-10 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='options',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='source',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='options',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 10, 17, 49, 30, 445771)),
        ),
    ]
