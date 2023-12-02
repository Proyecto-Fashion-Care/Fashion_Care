from django.shortcuts import render
import serial
import time
from datetime import datetime, timedelta
from newsapi import NewsApiClient  # Asegúrate de que newsapi esté instalado
from .forms import NewsForm
import requests

# Create your views here.
def home(request):
    try:
        ser = serial.Serial('COM9', 9600)  
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'1')
        print('portada')
        ser.close()
    finally:
        return render(request, 'core/index.html')

def api(request):
    try:
        ser = serial.Serial('COM9', 9600)  
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'2')  
        print('api')
        ser.close()
    finally:
        return render(request, 'core/api.html')

def inicio(request):
    try:
        ser = serial.Serial('COM9', 9600)  
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'4') 
        print('inicio')
        ser.close()
    finally:
        return render(request, 'core/inicio.html')
    
def noticias(request):
    if request.method == 'POST':
        # Crea una instancia del formulario y rellena los campos con la información de la solicitud
        form = NewsForm(request.POST)

        # Valida el formulario
        if form.is_valid():
            # Obtiene el tema de las noticias
            theme = form.cleaned_data['theme']
            

            # Obtiene la fecha actual
            current_date = datetime.now()
            newsapi = NewsApiClient(api_key="9aaaf2a83e8b4c59a2fac9ae1dcf58a8")
            # Realiza la solicitud a la API
            data = newsapi.get_everything(q=theme, language='es', sort_by='relevancy', page_size=100)

            # Obtiene la lista de artículos
            articles = data['articles']

            # Filtra las noticias que tienen menos de dos días de antigüedad
            filtered_news = [article for article in articles if
                             (current_date - datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")) > timedelta(days=2)]

            context = {'filtered_news': filtered_news}
            return render(request, 'core/noticias.html/', context)
    else:
        form = NewsForm()
    
    context = {'form': form}
    return render(request, 'core/noticias.html/', context)

