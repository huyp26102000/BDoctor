class XrayImage:
    ID = None
    patientID = None
    URLImage = None
    imageTime = None
    symptom = None
    imageDirection = None #frontal or lateral
    imageSide = None # AP or PA
    def __init__(self, ID, patientID, URLImage, imageTime, symptom, imageDirection, imageSide):
        self.ID = ID
        self.patientID = patientID
        self.URLImage = URLImage
        self.imageTime = imageTime
        self.symptom = symptom
        self.imageDirection = imageDirection
        self.imageSide = imageSide