from rest_framework import routers
from .views import CustomerViewSet, ServiceRequestViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = router.urls
