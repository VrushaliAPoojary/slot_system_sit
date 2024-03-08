# Generated by Django 5.0 on 2024-03-08 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_places_alter_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.places'),
            preserve_default=False,
        ),
    ]
