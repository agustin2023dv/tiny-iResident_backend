# models/unit.py
from django.db import models
from .user import User

class Unit(models.Model):
    building_name = models.CharField(max_length=100)
    floor = models.CharField(max_length=10)
    unit_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    type = models.CharField(
        max_length=20,
        choices=[('apartment', 'Apartment'), ('house', 'House')],
        default='apartment',
    )

    resident = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='unit')
    is_occupied = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('building_name', 'floor', 'unit_number')

    def __str__(self):
        return f"{self.building_name} - Unit {self.unit_number}, Floor {self.floor}"
