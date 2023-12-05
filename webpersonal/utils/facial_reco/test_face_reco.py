import cv2
import os
import mediapipe as mp
import serial
from statistics import mode

'''
#Iniciamos el puerto serial
ser = serial.Serial('COM9', 9600)
time.sleep(1)  # Esperamos 1 segundos
'''

dataPath = "facial_reco/DatasetFaces"
dir_list = os.listdir(dataPath)


mp_face_detection = mp.solutions.face_detection #Para detectar rostros
LABELS = dir_list #usuarios que hemos entrenado

# Leemos el modelo
face_reco = cv2.face.LBPHFaceRecognizer_create()
face_reco.read("facial_reco/LBPHFaceModel.xml")

#face_reco = cv2.face.EigenFaceRecognizer_create()
#face_reco.read("facial_reco/eigenFaceModel.xml")

#face_reco = cv2.face.FisherFaceRecognizer_create()
#face_reco.read("facial_reco/fisherFaceModel.xml")

# Inicializamos la camara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

moda = [] # Futura lista con la que obtendremos la moda de los resultados del reconocimiento facial

with mp_face_detection.FaceDetection(
     min_detection_confidence=0.5) as face_detection:

     while True:
          #Leemos la imagen de la camara: ret = True si se leyo correctamente y frame es la imagen
          ret, frame = cap.read()
          if ret == False: 
               break
          frame = cv2.flip(frame, 1) #Volteamos la imagen horizontalmente
          height, width, _ = frame.shape # _ se usa para ignorar el color
          frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Convertimos la imagen a RGB
          results = face_detection.process(frame_rgb) #Procesamos la imagen, usando un modelo para detectar caras

          if results.detections is not None: #Detectamos caritas
               for detection in results.detections:
                    #Coordenadas de la carita detectada
                    #anchura minima del fotograma donde se detecta la cara, y se multiplica por el ancho de la imagen
                    xmin = int(detection.location_data.relative_bounding_box.xmin * width) 
                    ymin = int(detection.location_data.relative_bounding_box.ymin * height) #idem pa la altura
                    #anchura y altura de la cara detectada
                    w = int(detection.location_data.relative_bounding_box.width * width)
                    h = int(detection.location_data.relative_bounding_box.height * height)
                    if xmin < 0 and ymin < 0: #A veces xmin y ymin son negativos, no se por que pasa esto
                         continue
                    #Crea una rectangulo alrededor de la cara detectada, de color verde y de grosor 5
                    #cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), (0, 255, 0), 5)
                    #Creamos una imagen con la cara detectada (dentro del rectangulo que detecta la cara)
                    face_image = frame[ymin : ymin + h, xmin : xmin + w]
                    #Si no se detecta la cara, continuamos para evitar que de error
                    if face_image.size == 0:
                         continue
                    #Convertimos la imagen a escala de grises(reducir el procesamiento de la imagen) y la redimensionamos a 72x72 pixeles
                    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                    face_image = cv2.resize(face_image, (72, 72), interpolation=cv2.INTER_CUBIC)
                    #cv2.imshow("Face", face_image) #Mostramos la imagen redimensionada, en blanco y negro

                    #Predecimos la imagen, para verificar al usuario
                    result = face_reco.predict(face_image)
                    #Ponemos texto alrededor del rectangulo, con el resultado de la prediccion
                    cv2.putText(frame, "{}".format(result), (xmin, ymin - 5), 1, 1.3, (210, 124, 176), 1, cv2.LINE_AA)
                    
                    #verde si detectamos al usuario y rojo si no 
                    if result[1] <= 140:
                         try:
                              color = (0, 255, 0) 
                              usuario = LABELS[result[0]]
                              #ser.write(b'1')
                         except:
                              continue                              
                    else:
                         color = (0, 0, 255)
                         usuario = 'Desconocido'
                         #ser.write(b'2')

                    cv2.putText(frame, f"{usuario}", (xmin, ymin - 15), 2, 1, color, 1, cv2.LINE_AA) #Mostramos el usuario
                    cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), color, 2) #Mostramos el rectangulo que detecta la cara
                    moda.append(usuario)

          cv2.imshow("Frame", frame)
          k = cv2.waitKey(1)
          if k == 27: #Si le damos al escape (Esc) salimos del programa
               break


cap.release()
cv2.destroyAllWindows()
#ser.close() #Cerramos el puerto serial

moda = mode(moda) #Obtenemos la moda de los resultados del reconocimiento facial
print(moda) #Mostramos la moda