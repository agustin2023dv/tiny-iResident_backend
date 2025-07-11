from rest_framework import viewsets, permissions
from core.models import WorkOrder
from core.serializers import WorkOrderSerializer

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'resident':
            return WorkOrder.objects.filter(user=user)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
