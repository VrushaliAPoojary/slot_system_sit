from django.db import models
from datetime import datetime, time

class Event(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(default=datetime(1970, 1, 1))
    start_time = models.DateTimeField(default=datetime(1970, 1, 1))  # Default to '00:00:00'
    end_time = models.DateTimeField(default=datetime(1970, 1, 1))  # Default to '00:00:00'
    image = models.ImageField(upload_to='event')


class places(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='place_photo')
    def __str__(self) -> str:
        return self.name