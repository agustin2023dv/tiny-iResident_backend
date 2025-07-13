# core/views/recertification_view.py

from rest_framework import viewsets, permissions
from core.models.recertification import RecertificationDocument
from core.serializers.recertification_serializer import RecertificationSerializer

class RecertificationViewSet(viewsets.ModelViewSet):
    queryset = RecertificationDocument.objects.all()
    serializer_class = RecertificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
