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
          #print(image_path)
          image = cv2.imread(image_path, 0)
          #cv2.imshow("Image", image)  #Para mostrar la imagen
          #cv2.waitKey(10) #Delay de 10 ms

          facesData.append(image)
          labels.append(label)
     label += 1

for i in range(len(dir_list)):
     print(dir_list[i] + ": ", np.count_nonzero(np.array(labels) == i)) #Numero de imagenes por usuario

# LBPH FaceRecognizer
face_reco = cv2.face.LBPHFaceRecognizer_create()

# Eigen FaceRecognizer
#face_reco = cv2.face.EigenFaceRecognizer_create()

# Fisher FaceRecognizer
#face_reco = cv2.face.FisherFaceRecognizer_create()

# Entrenamiento
print("Entrenando...")
face_reco.train(facesData, np.array(labels))

# Almacenar modelo
face_reco.write("facial_reco/LBPHFaceModel.xml")
#face_reco.write("facial_reco/eigenFaceModel.xml")
#face_reco.write("facial_reco/fisherFaceModel.xml")
print("Modelo almacenado")