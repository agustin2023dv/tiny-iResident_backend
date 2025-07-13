# views/work_order_view.py

from rest_framework import viewsets
from core.models import WorkOrder
from core.serializers.work_order import WorkOrderSerializer

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all().order_by('-created_at')
    serializer_class = WorkOrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
