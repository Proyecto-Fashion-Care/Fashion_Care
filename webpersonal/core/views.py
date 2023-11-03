from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    html_response = "<h1>Mi Web Personal</h1>"
    for _ in range(10):
        html_response += "<p>Hola Mundo</p>"
    return HttpResponse(html_response)
