import cv2
import os
import mediapipe as mp


mp_face_detection = mp.solutions.face_detection #Para detectar rostros

user = input('usuario: ')
output_folder = f'facial_reco/DatasetFaces/{user}'

# Verificar si la carpeta existe, si no, crearla
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

counter = 300

# Inicializamos la camara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_face_detection.FaceDetection(
     min_detection_confidence=0.5) as face_detection:

     while counter <= 400:
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
                    cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), (0, 255, 0), 5)
                    #Creamos una imagen con la cara detectada (dentro del rectangulo que detecta la cara)
                    face_image = frame[ymin : ymin + h, xmin : xmin + w]
                    #Si no se detecta la cara, continuamos para evitar que de error
                    if face_image.size == 0:
                         continue
                    #Convertimos la imagen a escala de grises(reducir el procesamiento de la imagen) y la redimensionamos a 72x72 pixeles
                    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                    face_image = cv2.resize(face_image, (72, 72), interpolation=cv2.INTER_CUBIC)
                    #cv2.imshow("Face", face_image) #Mostramos la imagen redimensionada, en blanco y negro
                    #Guardamos una imagen, cada 10 segundos
                    if counter <= 400:
                        img = f'{user}{counter}.jpg'
                        ruta_imagen = os.path.join(output_folder, img)
                        cv2.imwrite(ruta_imagen, face_image)
                    else:
                         break
                    counter += 1


          cv2.imshow("Frame", frame)
          k = cv2.waitKey(1)
          if k == 27: #Si le damos al escape (Esc) salimos del programa
               break
cap.release()
cv2.destroyAllWindows()