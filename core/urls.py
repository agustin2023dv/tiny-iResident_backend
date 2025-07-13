from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UnitViewSet, WorkOrderViewSet
from core.views.recertification_view import RecertificationViewSet 

router = DefaultRouter()
router.register(r'units', UnitViewSet)
router.register(r'work-orders', WorkOrderViewSet)
router.register(r'recertifications', RecertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
