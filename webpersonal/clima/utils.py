import requests

def obtener_datos_clima():
    api_key = "beca443305c5fcb28b732af45d0b0114"  # Reemplaza con tu clave API
    city = input("Ingresa tu ciudad: ")
    
    # Agrega el parámetro lang=es para obtener datos en español
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=es"

    res = requests.get(url)
    data = res.json()

    if res.status_code == 200:
        # Convierte la temperatura de Kelvin a Celsius
        temperatura_celsius = data['main']['temp'] - 273.15

        # Asegúrate de explorar la estructura de 'data' y extraer la información necesaria
        print("Datos del tiempo:")
        print(f"Temperatura: {temperatura_celsius:.2f}°C")
        print(f"Condición: {data['weather'][0]['description']}")
        print(f"Humedad: {data['main']['humidity']}%")
        print(f"Viento: {data['wind']['speed']} m/s")
    else:
        print(f"Error: No se pudieron obtener datos del tiempo para {city}")

