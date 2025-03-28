from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.manage_requests, name='manage_requests'),
    path('resolve/<int:request_id>/', views.resolve_request, name='resolve_request'),
]
