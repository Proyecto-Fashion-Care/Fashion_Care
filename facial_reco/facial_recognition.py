import numpy as np
import cv2
import os

class facialRecognition:

    def __init__(self, dataPath) -> None:
        self.dataPath = dataPath
        self.dir_list = os.listdir(self.dataPath) #Carpetas dentro del path (usuarios)


    def train(self):
        print("Lista archivos:", self.dir_list)

        labels = [] #Etiquetas asignadas a las imagenes
        facesData = [] #Rostros detectados
        label = 0 

        for name_dir in self.dir_list:
            dir_path = self.dataPath + "/" + name_dir
            
            for file_name in os.listdir(dir_path):
                image_path = dir_path + "/" + file_name
                #print(image_path)
                image = cv2.imread(image_path, 0)
                #cv2.imshow("Image", image)  #Para mostrar la imagen
                #cv2.waitKey(10) #Delay de 10 ms

                facesData.append(image)
                labels.append(label)
            label += 1

        for i in range(len(self.dir_list)):
            print(self.dir_list[i] + ": ", np.count_nonzero(np.array(labels) == i)) #Numero de imagenes por usuario

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

        


facialReco = facialRecognition("facial_reco/DatasetFaces")