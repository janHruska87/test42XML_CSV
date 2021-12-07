import csv
import datetime
import xml.etree.ElementTree as ET
from datetime import datetime

import Objects
from Objects import TestCase as TC
from Objects import TestCaseEntry as TCE
import socket


def writeToCSV(body,header):
    "Write result to CSV file"
    with open(getFilename(),"w") as outFile:
        "Settings for CSV writer, write header dict"
        writer = csv.writer(outFile, delimiter=";")
        writer.writerow(header.values())

        for tc in body:
            writer.writerow(TC.toString(tc))

def getFilename():
    filename = "/home/jan/Dokumenty/" + datetime.now().strftime("%Y-%m-%d-%H-%M") + ".csv"
    return filename

def parse(file):
    content = open(file, "r")
    tree = ET.parse(content)
    root = tree.getroot()
    header = {1: "Id",2:"T42ObjectId",3:"T42ObjectVersionId",4:"name",5:"Version",6:"CreationDate",7:"DOORSId",8:"Automation",9:"TestObjectCategory",10:"TestType",11:"TestDepth",12:"SpecialFeature",13:"TestCaseEntries"}
    #testCases = root.iter("TestCases")
    #functions = root.iter("Functions")
    testCases = list()
    for child in root:
        if child.tag == "{http://test42.sys42.vwg/emx}TestCases":
            for tc in child:
                testCase = TC()
                testCase.id = tc.attrib[header[1]]
                testCase.T42ObjectId = tc.attrib[header[2]]
                testCase.T42ObjectVersionId = tc.attrib[header[3]]
                for tcc in tc:
                    if tcc.tag.endswith(header[4]):
                        testCase.name = tcc.text
                    elif tcc.tag.endswith(header[5]):
                        testCase.version = tcc.text
                    elif tcc.tag.endswith(header[6]):
                        testCase.creationDate = tcc.text
                    elif tcc.tag.endswith(header[7]):
                        testCase.creationDate = tcc.text
                    elif tcc.tag.endswith(header[8]):
                        testCase.automation = tcc.text
                    elif tcc.tag.endswith(header[9]):
                        testCase.testObjectCategory = tcc.text
                    elif tcc.tag.endswith(header[10]):
                        testCase.testType = tcc.text
                    elif tcc.tag.endswith(header[11]):
                        testCase.testDepth = tcc.text
                    elif tcc.tag.endswith(header[12]):
                        testCase.specialFeature = tcc.text
                    elif tcc.tag.endswith(header[13]):
                        "Vsechny TC v ramci jednoho TC, objekt TestCaseEntries "
                        for tccc in tcc:
                            testCaseEntry = TCE()
                            testCaseEntry.type = tccc.attrib["Type"]
                            for tcccc in tccc:
                                "Nahrani [index, text] z TestCaseEntry"
                                if tcccc.tag.endswith("Text"):
                                    testCaseEntry.text = tcccc.text
                                elif tcccc.tag.endswith("Index"):
                                    testCaseEntry.index = int(tcccc.text)
                            testCase.testCaseEntries.append(testCaseEntry)
                testCases.append(testCase)

    writeToCSV(testCases,header)
    print("Nahrano: ", testCases.__len__())
    return testCases
