
from django.shortcuts import render
from .utils import obtener_datos_clima

def obtener_clima(request):
    if request.method == 'POST':
        ciudad = request.POST.get('ciudad', '')
        datos_clima = obtener_datos_clima(ciudad)
        return render(request, 'clima_resultado.html', {'datos_clima': datos_clima})

    return render(request, 'clima_formulario.html')
