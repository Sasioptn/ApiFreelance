from django.db import models
from users.models import CustomUser


class Order(models.Model):
    title = models.CharField(max_length=480)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, related_name='owner', on_delete=models.CASCADE)
    developer = models.ForeignKey(CustomUser, related_name='executor', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('created',)
