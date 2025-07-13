# models/recertification.py

from django.db import models
from .user import User
from .unit import Unit

class RecertificationDocument(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='recertifications')
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    document = models.FileField(upload_to='recertifications/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.unit} - {self.status} - {self.uploaded_at.date()}"
