# Generated by Django 5.0 on 2024-02-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='Event'),
        ),
    ]
