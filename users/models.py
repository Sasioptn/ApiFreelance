from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_ROLE = [
        ('customer', 'customer'),
        ('executor', 'executor')
    ]
    balance = models.DecimalField(max_digits=100, decimal_places=10, default=0.0)
    user_role = models.CharField(max_length=10,choices=USER_ROLE)
