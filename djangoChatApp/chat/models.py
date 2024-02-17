from django.db import models
from datetime import datetime

# Create your models here.
#create models for chat room

class Room(models.Model):
    name = models.CharField(max_length=1000)

#create models for messages
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)