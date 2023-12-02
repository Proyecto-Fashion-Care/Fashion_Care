import cv2
import os
import numpy as np

dataPath = "facial_reco/Img"
dir_list = os.listdir(dataPath)
print("Lista archivos:", dir_list)

labels = [] #Etiquetas asignadas a las imagenes
facesData = [] #Rostros detectados
label = 0 

for name_dir in dir_list:
     dir_path = dataPath + "/" + name_dir
     
     for file_name in os.listdir(dir_path):
          image_path = dir_path + "/" + file_name
          print(image_path)
          image = cv2.imread(image_path, 0)
          #cv2.imshow("Image", image)  #Para mostrar la imagen
          #cv2.waitKey(10) #Delay de 10 ms

          facesData.append(image)
          labels.append(label)
     label += 1

for i in range(label):
     print("Etiqueta ", i, ": ", np.count_nonzero(np.array(labels) == i)) #Numero de rostros por etiqueta

# LBPH FaceRecognizer
face_mask = cv2.face.LBPHFaceRecognizer_create()

# Entrenamiento
print("Entrenando...")
face_mask.train(facesData, np.array(labels))

# Almacenar modelo
face_mask.write("facial_reco/face_mask_model.xml")
print("Modelo almacenado")