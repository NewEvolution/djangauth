from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

USER_TYPES = [('cogmaker', 'Cog Maker'), ('coguser', 'Cog User')]

class User(AbstractUser):
    usertype = models.CharField(choices=USER_TYPES, max_length=8)

    def __str__(self):
        return self.username


class Cog(models.Model):
    name = models.CharField(max_length=32)
    tooth_count = models.IntegerField(default=4)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cogs')

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notes')

    def __str__(self):
        return self.title


class PersonalNote(Note):
    pass
