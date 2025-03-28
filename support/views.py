from django.shortcuts import render,redirect, get_object_or_404
from customer.models import ServiceRequest

def manage_requests(request):
    requests = ServiceRequest.objects.filter(status='submitted')
    return render(request, 'support/manage_requests.html', {'requests': requests})

def resolve_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    service_request.status = 'resolved'
    service_request.save()
    return redirect('manage_requests')
