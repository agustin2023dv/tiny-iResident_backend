from django.db import models
from .user import User

class Unit(models.Model):
    address = models.CharField(max_length=255)
    resident = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.address
