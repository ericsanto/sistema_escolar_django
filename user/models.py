from django.db import models
from django.contrib.auth.models import AbstractUser


class UserCustom(AbstractUser):
    registration = models.CharField(max_length=15, unique=True)

    USERNAME_FIELD = 'registration'
    REQUIRED_FIELDS = 'username',
