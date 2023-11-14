from django.shortcuts import render
import serial
import time

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
        ser.write(b'3') 
        print('inicio')
        ser.close()
    finally:
        return render(request, 'core/inicio.html')