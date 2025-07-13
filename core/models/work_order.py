# models/work_order.py
from django.db import models
from .user import User
from .unit import Unit

# models/work_order.py

class WorkOrder(models.Model):
    AREA_TYPE_CHOICES = [
        ('UNIT', 'Unit'),
        ('COMMON_AREA', 'Common Area'),
    ]

    JOB_TYPE_CHOICES = [
        ('plumbing', 'Plumbing'),
        ('electrical', 'Electrical'),
        ('hvac', 'HVAC'),
        ('other', 'Other'),
    ]

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='work_orders')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    area_type = models.CharField(max_length=50, choices=AREA_TYPE_CHOICES)
    area_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='work_orders/', null=True, blank=True)
    permission_to_enter = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_type} - {self.unit} - {self.status}"

