from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)


class user(models.Model):
    id = models.UUIDField(primary_key=True, default=None)
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)