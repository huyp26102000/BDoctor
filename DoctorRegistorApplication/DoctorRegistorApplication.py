from ModuleImport import *
import sys, os, shutil
from distutils.dir_util import copy_tree


#######################################################################
# TITLEBAR FUNCTION
#######################################################################
def setupTitleBar(ui):
    ui.loginFrom_btnClose.clicked.connect(closeWindow)
    ui.loginFrom_btnMinimize.clicked.connect(minimizeWindow)
def closeWindow():
    sys.exit()
def minimizeWindow():
    MainWindow.showMinimized()

#######################################################################
# file function
#######################################################################

def getFileNameFromPath(xfilePath):
    max = len(xfilePath)
    fileName = ""
    for i in range(max-1, 0, -1):
        if xfilePath[i] == '/':
            break
        fileName+=xfilePath[i]
    fileName = fileName[::-1]
    return fileName
def loadFiles():
    filter = "All file (*);;JPG (*.jpg);;PNG (*.png)"
    dialog = QtWidgets.QFileDialog()
    dialog.setWindowTitle("Select File")
    dialog.setNameFilter(filter)
    dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
    file_full_path = ""
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        file_full_path+=str(dialog.selectedFiles())
    else:
        return None
    filePath = file_full_path.split(',')
    for i in range(0, len(filePath)):
        tmp = filePath[i]
        tmp = tmp.replace("'", '')
        tmp = tmp.replace('[', '')
        tmp = tmp.replace(']', '')
        tmp = tmp.replace(' ', '')
        filePath[i] = tmp
    return filePath
def loadRawImage(AvatarPath):
    currentPath = os.getcwd()
    imp_OutputPathFile = currentPath + "/DoctorRegistorApplication/DataImageUser/Doctor/"
    # rawImagePath = currentPath + "//dataImage//OriginalXrayImage//"
    filePath = loadFiles()
    if filePath!=None:
        for tmp in filePath:
            tmp_filename = getFileNameFromPath(tmp)
            outputPathFile = imp_OutputPathFile + getRandomText() + '.jpg'
            shutil.copy2(tmp, outputPathFile)
        ui_RegDocForm.AvatarPath = outputPathFile
        updateAvatar(ui_RegDocForm.AvatarPath)
def updateAvatar(avatarPath):
    avatarPixmap = QtGui.QPixmap(avatarPath)
    avatarPixmap = resizePixmap(avatarPixmap, ui_RegDocForm.loginFrom_LbAvatar)
    ui_RegDocForm.loginFrom_LbAvatar.setPixmap(avatarPixmap)
def resizePixmap(inPixmap, label):
    labelWidth   = label.width()
    labelHeight  = label.height()
    pixmapWidth  = inPixmap.width()
    pixmapHeight = inPixmap.height()
    ratioLabel   = labelWidth/labelHeight
    ratioPixmap  = pixmapWidth/pixmapHeight
    # inPixmap.scaledToHeight(pixmapHeight)
    # resize
    if ratioPixmap > ratioLabel:
        tmp_pixmapWidth = pixmapWidth
        pixmapWidth = labelWidth
        pixmapHeight = (labelWidth*pixmapHeight)/tmp_pixmapWidth
    else:
        if ratioPixmap < ratioLabel:
            tmp_pixmapHeight = pixmapHeight
            pixmapHeight = labelHeight
            pixmapWidth = (labelHeight*pixmapWidth)/tmp_pixmapHeight
    inPixmap = inPixmap.scaled(pixmapWidth, pixmapHeight)
    return inPixmap


# ADDING INFORMATION FUNCTION
#######################################################################
# Experience
def addExperience():
    textDescription = ui_RegDocForm.loginFrom_TbDes.toPlainText()
    textYear = ui_RegDocForm.loginFrom_CbbNumyear.currentText()
    objExperience = ExperienceAtribute(textDescription, textYear)
    drProfile.totalExperience.append(objExperience)
    updateExperience(drProfile)
def updateExperience(drProfile):
    numberOfEx = len(drProfile.totalExperience)
    for i in range(0, numberOfEx):
        ui_RegDocForm.loginFrom_ExList.setItem(i+1, 0, QtWidgets.QTableWidgetItem(drProfile.totalExperience[i].description))
        ui_RegDocForm.loginFrom_ExList.setItem(i+1, 1, QtWidgets.QTableWidgetItem(drProfile.totalExperience[i].numberOfYear))
        ui_RegDocForm.loginFrom_TbDes.setPlainText('')
        ui_RegDocForm.loginFrom_CbbNumyear.setCurrentIndex(0)
# Achiverment
def addAchiverment():
    textDescription = ui_RegDocForm.loginFrom_TbDes2.toPlainText()
    textYear = ui_RegDocForm.loginFrom_CbbNumyearAchir.currentText()
    objAchiverment = AchivermentAtribute(textDescription, textYear)
    drProfile.totalAchiverment.append(objAchiverment)
    updateAchiverment(drProfile)
def updateAchiverment(drProfile):
    numberOfAchiv = len(drProfile.totalAchiverment)
    for i in range(0, numberOfAchiv):
        ui_RegDocForm.loginFrom_AchirveList.setItem(i+1, 0, QtWidgets.QTableWidgetItem(drProfile.totalAchiverment[i].description))
        ui_RegDocForm.loginFrom_AchirveList.setItem(i+1, 1, QtWidgets.QTableWidgetItem(drProfile.totalAchiverment[i].year))
        ui_RegDocForm.loginFrom_TbDes2.setPlainText('')
        ui_RegDocForm.loginFrom_CbbNumyearAchir.setCurrentIndex(0)
#######################################################################
# END OF ADDING INFORMATION FUNCTION
def RegisterAccount():
    drProfile.familyName = str(ui_RegDocForm.loginFrom_TbFirstname.toPlainText())
    drProfile.lastName = str(ui_RegDocForm.loginFrom_TbLastname.toPlainText())
    drProfile.email = str(ui_RegDocForm.loginFrom_TbEmail.toPlainText())
    drProfile.PhoneNumber = str(ui_RegDocForm.loginFrom_tbPhoneNumber.toPlainText())
    drProfile.MedicalMajor = str(ui_RegDocForm.loginFrom_CbbMajor.currentText())
    drProfile.avatarURL = ui_RegDocForm.AvatarPath
    drProfile.birthYear = str(ui_RegDocForm.loginFrom_CbbBirthyear.currentText())
    drProfile.homeTown = str(ui_RegDocForm.loginFrom_TbHometown.toPlainText())
    drProfile.currentWorkingLocation = str(ui_RegDocForm.loginFrom_TbCurrentWorkLocation.toPlainText())
    drProfile.education = str(ui_RegDocForm.loginFrom_TbEducation.toPlainText())
    checkNoneAtribute(drProfile)
    DBConnector.registorAccount(drProfile)

def checkNoneAtribute(drProfileObj):
    if(drProfileObj.familyName == None or drProfileObj.familyName == ''):
        popupShowMessage("Please fill First name.")
    else:
        if(drProfileObj.lastName == None or drProfileObj.lastName == ''):
            popupShowMessage("Please fill Last name.")
        # else:
        #     if(drProfileObj.email == None or drProfileObj.email == ''):
        #         popupShowMessage("Please fill email.")
        #     else:
        #         if(drProfileObj.PhoneNumber == None or drProfileObj.PhoneNumber == ''):
        #             popupShowMessage("Please fill PhoneNumber.")
        #         else:
        #             if(drProfileObj.avatarURL == None or drProfileObj.avatarURL == ''):
        #                 popupShowMessage("Please choose picture for profile.")
        #             else:
        #                 if(drProfileObj.homeTown == None or drProfileObj.homeTown == ''):
        #                     popupShowMessage("Please fill homeTown.")
        #                 else:
        #                     if(drProfileObj.currentWorkingLocation == None or drProfileObj.currentWorkingLocation == ''):
        #                         popupShowMessage("Please provide current working location.")
        #                     else:
        #                         if(drProfileObj.education == None or drProfileObj.education == ''):
        #                             popupShowMessage("Please provide education detail.")


#######################################################################
# POPUP WINDOW
#######################################################################
def popupShowMessage(message):
    ui_error_popup.errorPopup_lbMessage.setText(message)
    popupWindow.show()
def hidePopupWindow():
    popupWindow.hide()
#######################################################################
# END OF POPUP WINDOW

if __name__ == "__main__":
    drProfile = DoctorProfile(None, None, None, None, None, None, None, None, None, None, None)
    # Setup main form
    #######################################################################
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_RegDocForm = UI_DoctorRegMainForm()
    ui_RegDocForm.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # Setup titlebar
    setupTitleBar(ui_RegDocForm)
    # Setup Error Popup
    popupWindow = QtWidgets.QMainWindow()
    ui_error_popup = ErrorPopup()
    ui_error_popup.setupUi(popupWindow)
    popupWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui_error_popup.btn_OK.clicked.connect(hidePopupWindow)
    #######################################################################
    # Setup Database
    DBConnector = AppConnector("localhost", "root", "lemon", "bdoctordb")
    DBConnector.connectTodataBase()
    #######################################################################
    # Component event
    # load avatar
    ui_RegDocForm.loginFrom_btnChoose.clicked.connect(loadRawImage)
    # add achiverment
    ui_RegDocForm.loginFrom_btnSubmit2.clicked.connect(addAchiverment)
    # add Experience
    ui_RegDocForm.loginFrom_btnSubmitEx.clicked.connect(addExperience)
    # cursor = QtGui.QTextCursor()
    # ui_RegDocForm.loginFrom_TbFirstname.setTextCursor(cursor)
    # validator = QtGui.validator(regex)
    # ui_RegDocForm.loginFrom_TbFirstname.setValidator(validator)
    # final Register
    ui_RegDocForm.loginFrom_btnReg.clicked.connect(RegisterAccount)
    #######################################################################
    MainWindow.show()
    sys.exit(app.exec_())
