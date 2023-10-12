from django.db import models
from django.contrib.auth.models import User

class ReserveMeetingRoom(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title