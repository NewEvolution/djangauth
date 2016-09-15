from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

USER_TYPES = [('cogmaker', 'Cog Maker'), ('coguser', 'Cog User')]

class User(AbstractUser):
    usertype = models.CharField(choices=USER_TYPES, max_length=8)


class Cog(models.Model):
    name = models.CharField(max_length=32)
    tooth_count = models.IntegerField(default=4)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cogs')
