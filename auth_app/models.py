from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    phone = models.CharField(max_length=100, null=True, blank=True)