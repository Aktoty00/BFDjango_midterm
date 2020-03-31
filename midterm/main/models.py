from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class MyUser(AbstractUser):
    USER_ROLES = (
        ('SuperAdmin', 'SuperAdmin'),
        ('Guest', 'Guest')
    )
    role = models.CharField(choices=USER_ROLES, max_length=200, default='Guest')


class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)


class Role(models.Model):
    name = models.CharField(max_length=200)
