import re
import requests
import os

translateAPI = "https://www.googleapis.com/language/translate/v2?key=[Your Key Here]"

def createDirectoryIfNotExists(fileName):
    if not os.path.exists(os.path.dirname(fileName)):
        os.makedirs(os.path.dirname(fileName))

def getNameOfOutputFile(targetName):
	return "flatTextOutput/" + targetName

def writeToFile(translatedText, targetName):
    fileName = getNameOfOutputFile(targetName)
    createDirectoryIfNotExists(fileName)
    with open(fileName, "a") as myfile:
    	contentToWrite = translatedText + "\n"
        myfile.write(contentToWrite)

def translateSourceText(sourceText, target):
    url = translateAPI + "&q=" + sourceText + "&source=en&target=" + target
    r = requests.get(url)
    jsonObject = jsonObject = r.json()
    return jsonObject['data']['translations'][0]['translatedText'].encode('utf-8')

def translateLineInFile(line, target, translateName):
    translation = translateSourceText(line, target)
    writeToFile(translation, translateName)

def clearContentsOfFile(translateName):
    fileName = getNameOfOutputFile(translateName)
    createDirectoryIfNotExists(fileName)
    open(fileName, 'w').close()

def translateFile(translateName, target):

    print("Translating for: " + translateName)

    clearContentsOfFile(translateName)

    with open('flatText.txt', 'r') as stringsFile:
        for line in stringsFile:
            translateLineInFile(line, translateTarget, translateName)


with open('Google_IOS_Country_Codes.txt', 'r') as targetsFile:
    for targetLine in targetsFile:
        
        if "#" in targetLine:
            continue

    	targetArray = targetLine.split()

    	translateName = targetArray[0]
    	translateTarget = targetArray[1]

        translateFile(translateName, translateTarget)


