from django.db import models
from datetime import datetime

class places(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='place_photo')

    def __str__(self) -> str:
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(default=datetime(1970, 1, 1))
    start_time = models.DateTimeField(default=datetime(1970, 1, 1))
    end_time = models.DateTimeField(default=datetime(1970, 1, 1))
    image = models.ImageField(upload_to='event')
    place = models.ForeignKey(places, on_delete=models.CASCADE)
