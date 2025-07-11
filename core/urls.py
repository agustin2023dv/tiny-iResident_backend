from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UnitViewSet, WorkOrderViewSet 

router = DefaultRouter()
router.register(r'units', UnitViewSet)
router.register(r'work-orders', WorkOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
