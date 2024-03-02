# Generated by Django 5.0 on 2024-02-20 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_event_end_time_event_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
