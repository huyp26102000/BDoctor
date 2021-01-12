class DoctorProfile:
    ID = None
    familyName = None
    lastName = None
    email = None
    PhoneNumber = None
    MedicalMajor = None
    totalExperience = []
    totalAchiverment = []
    avatarURL = None
    birthYear = None
    homeTown = None
    currentWorkingLocation = None
    education = None
    def __init__(self, ID, familyName, lastName, email, 
                    PhoneNumber, MedicalMajor, avatarURL, 
                    birthYear, homeTown, currentWorkingLocation, education):
        self.ID = ID
        self.familyName = familyName
        self.lastName = lastName
        self.email = email
        self.PhoneNumber = PhoneNumber
        self.MedicalMajor = MedicalMajor
        self.avatarURL = avatarURL
        self.homeTown = homeTown
        self.currentWorkingLocation = currentWorkingLocation
        self.education = education

class ExperienceAtribute:
    description = None
    numberOfYear = None
    def __init__(self, description, numberOfYear):
        self.description = description
        self.numberOfYear = numberOfYear
class AchivermentAtribute:
    description = None
    year = None
    def __init__(self, description, year):
        self.description = description
        self.year = year