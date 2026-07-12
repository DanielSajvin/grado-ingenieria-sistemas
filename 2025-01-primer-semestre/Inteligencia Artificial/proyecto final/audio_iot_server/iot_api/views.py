from django.http import JsonResponse
from django.shortcuts import render


def about(request):
    return render(request, "iot_api/about.html")  # Include app prefix


def hello_world(request):
    return JsonResponse({"message": "Hello, World!"})
