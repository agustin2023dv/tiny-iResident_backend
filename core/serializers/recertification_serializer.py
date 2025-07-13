# core/serializers/recertification_serializer.py

from rest_framework import serializers
from core.models.recertification import RecertificationDocument

class RecertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecertificationDocument
        fields = '__all__'
        read_only_fields = ['status', 'submitted_at']
