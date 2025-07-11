from rest_framework import viewsets, permissions
from core.models import Unit
from core.serializers import UnitSerializer

class UnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]
