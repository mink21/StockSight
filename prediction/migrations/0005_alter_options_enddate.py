# Generated by Django 4.0.1 on 2022-01-10 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_alter_options_enddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 10, 18, 6, 28, 879638)),
        ),
    ]
