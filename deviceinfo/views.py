from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_system_info

def system_info_view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(get_system_info())
    return render(request, "deviceinfo/system_info.html")
