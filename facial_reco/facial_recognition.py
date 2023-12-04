import os

class facialRecognition:

    def __init__(self, dataPath) -> None:
        self.dataPath = dataPath
        self.dir_list = os.listdir(self.dataPath) #Carpetas dentro del path (usuarios)


facialReco = facialRecognition("facial_reco/DatasetFaces")