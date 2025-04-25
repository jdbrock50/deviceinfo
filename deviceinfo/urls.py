from django.urls import path
from .views import system_info_view

urlpatterns = [
    path('info/', system_info_view, name='device_info'),
]
