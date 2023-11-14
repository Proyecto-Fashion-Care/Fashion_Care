from django.shortcuts import render
import serial
import time

# Create your views here.
def home(request):
    try:
        ser = serial.Serial('COM9', 9600)  # Ajusta el puerto según tu configuración
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'1')  # Envía un byte para encender la luz
        print('portada')
        ser.close()
    finally:
        return render(request, 'core/index.html')

def api(request):
    try:
        ser = serial.Serial('COM9', 9600)  # Ajusta el puerto según tu configuración
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'2')  # Envía un byte para encender la luz
        print('api')
        ser.close()
    finally:
        return render(request, 'core/api.html')

def inicio(request):
    try:
        ser = serial.Serial('COM9', 9600)  # Ajusta el puerto según tu configuración
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'3')  # Envía un byte para encender la luz
        print('inicio')
        ser.close()
    finally:
        return render(request, 'core/inicio.html')