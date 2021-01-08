from ModuleImport import *
import sys, os, shutil
from datetime import datetime, date
import random

from distutils.dir_util import copy_tree
import time

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
def getRandomText():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%Ho%Mo%S")
    current_date = today.strftime("%mo%do%y")
    randomNumber = int(random.random()*100000000)
    randomText = str(current_date)+'o'+str(current_time)+'o'+str(randomNumber)
    return randomText
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
# get account name
def getAccountName(inputName):
    outputText = ''
    i = 0
    splitedText = inputName.split(' ')
    ReSplitedText = reversed(splitedText)

    for tmp in ReSplitedText:
        if i == 0:
            tmpText = str(tmp)
            outputText+=tmpText
        i+=1
    i = 0
    for tmp in splitedText:
        if i < len(splitedText)-1:
            tmpText = str(tmp)
            outputText+=tmpText[0]
        i+=1
    return outputText.lower()
if __name__ == "__main__":

    # Setup main form
    #######################################################################
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_RegDocForm = UI_DoctorRegMainForm()
    ui_RegDocForm.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # Setup titlebar
    setupTitleBar(ui_RegDocForm)

    #######################################################################
    # load avatar
    ui_RegDocForm.loginFrom_btnChoose.clicked.connect(loadRawImage)
    
    MainWindow.show()
    sys.exit(app.exec_())
