from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def api(request):
    return render(request, 'core/api.html')

def inicio(request):
    return render(request, 'core/inicio.html')