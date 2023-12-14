from gtts import gTTS
import pyaudio
import io

# Texto que deseas convertir a voz
texto = "Hola, ¿cómo estás?"

# Crear un objeto gTTS
tts = gTTS(text=texto, lang='es')

# Crear un objeto BytesIO para almacenar los datos de audio
buffer = io.BytesIO()

# Guardar los datos de audio en el objeto BytesIO
tts.write_to_fp(buffer)

# Obtener los datos de audio como bytes
audio_bytes = buffer.getvalue()

# Inicializar PyAudio
p = pyaudio.PyAudio()

# Definir los parámetros del formato de audio
formato = p.get_format_from_width(width=2)  # 16 bits por muestra
canales = 1  # Mono
tasa_muestreo = int(tts.estimated_time * 1000)  # Ajustar según sea necesario

# Abrir un flujo de audio
stream = p.open(format=formato,
                channels=canales,
                rate=tasa_muestreo,
                output=True)

# Reproducir el audio
stream.write(audio_bytes)

# Cerrar el flujo de audio y PyAudio
stream.stop_stream()
stream.close()
p.terminate()
