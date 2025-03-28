from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/submit_request.html', {'form': form})

def request_status(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer/request_status.html', {'requests': requests})
