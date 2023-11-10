from django.shortcuts import render, HttpResponse
import serial

# Create your views here.

def home(request):
    ser = serial.Serial('COM4', 9600)  # Ajusta el puerto según tu configuración
    ser.write(b'1')  # Envía un byte para encender la luz
    ser.close()
    return render(request, 'core/index.html')

def api(request):
    ser = serial.Serial('COM4', 9600)  # Ajusta el puerto según tu configuración
    ser.write(b'2')  # Envía un byte para encender la luz
    ser.close()
    return render(request, 'core/api.html')

def inicio(request):
    ser = serial.Serial('COM4', 9600)  # Ajusta el puerto según tu configuración
    ser.write(b'3')  # Envía un byte para encender la luz
    ser.close()
    return render(request, 'core/inicio.html')