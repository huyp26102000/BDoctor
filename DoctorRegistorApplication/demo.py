import os
demotext = "Pham Huy quoc nam"
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
