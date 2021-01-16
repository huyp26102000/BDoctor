import time
from datetime import datetime, date
import random
import hashlib

def getRandomText():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H%M%S")
    current_date = today.strftime("%m%d%y")
    randomNumber = int(random.random()*100000000)
    randomText = str(current_date)+'o'+str(current_time)+'o'+str(randomNumber)
    return randomText
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
def getCrytoPassword(password):
    h = hashlib.sha256(str(password).encode('utf-8'))
    return str(h.hexdigest())