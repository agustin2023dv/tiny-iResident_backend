from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UnitViewSet, WorkOrderViewSet
from core.views.auth_view import MeView
from core.views.recertification_view import RecertificationViewSet 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'units', UnitViewSet)
router.register(r'work-orders', WorkOrderViewSet)
router.register(r'recertifications', RecertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me/', MeView.as_view(), name='me'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
