from rest_framework import viewsets
from customer.models import ServiceRequest
from customer.serializers import ServiceRequestSerializer

class SupportRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
