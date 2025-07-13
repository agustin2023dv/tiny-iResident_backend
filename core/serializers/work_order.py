# serializers/work_order_serializer.py

from rest_framework import serializers
from core.models.work_order import WorkOrder

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'
        read_only_fields = ['id', 'status', 'created_at']
