import csv
import datetime
import xml.etree.ElementTree as ET
from datetime import datetime

import Objects
from Objects import TestCase as TC
from Objects import TestCaseEntry as TCE
import socket


def writeToCSV(body,header, outPutDirectory):
    "Write result to CSV file"
    with open(getFilename(outPutDirectory),"w") as outFile:
        "Settings for CSV writer, write header dict"
        writer = csv.writer(outFile, delimiter=";")
        writer.writerow(header.values())

        for tc in body:
            writer.writerows(TC.toString(tc))
            print(TC.toString(tc))

def sortTestCaseEntry(testCaseObject):
    sortedTestCaseEntry = list()
    i = 1
    while i <= testCaseObject.testCaseEntries.__len__() :
        for testCaseEntry in testCaseObject.testCaseEntries:
            if testCaseEntry.index == i:
                sortedTestCaseEntry.append(testCaseEntry)
                i += 1
    testCaseObject.testCaseEntries = sortedTestCaseEntry

    return testCaseObject


def getFilename(outPutDirectory):
    filename = outPutDirectory + datetime.now().strftime("%Y-%m-%d-%H-%M") + ".csv"
    return filename

def parse(file,outPutDirectory,comp,prio):
    content = open(file, "r")
    tree = ET.parse(content)
    root = tree.getroot()
    header = {1: "Id",2:"T42ObjectId",3:"T42ObjectVersionId",4:"Name",5:"Version",6:"CreationDate",7:"DOORSId",8:"Automation",9:"TestObjectCategory",10:"TestType",11:"TestDepth",12:"SpecialFeature",13:"TestCaseEntries",14:"Description",15:"Component",16:"Priorita"}
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
                testCase.component = comp
                testCase.priority = prio
                for tcc in tc:
                    if tcc.tag.endswith(header[4]):
                        testCase.name = tcc.text
                    elif tcc.tag.endswith(header[5]):
                        testCase.version = tcc.text
                    elif tcc.tag.endswith(header[6]):
                        testCase.creationDate = tcc.text
                    elif tcc.tag.endswith(header[7]):
                        testCase.dOORSId = tcc.text
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
                    elif tcc.tag.endswith(header[14]):
                        testCase.description = tcc.text
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

                "volame funkci na setrideni testcase entry podle hodnoty indexu"
                testCases.append(sortTestCaseEntry(testCase))

    writeToCSV(testCases,header,outPutDirectory)
    print("Nahrano: ", testCases.__len__())
    return testCases
