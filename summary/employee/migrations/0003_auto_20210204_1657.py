# Generated by Django 3.1.6 on 2021-02-04 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210204_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 16, 57, 22, 283763)),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 16, 57, 22, 283763)),
        ),
    ]
