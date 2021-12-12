
class TestCase:
    """Define full TestCase object. Must be include all fields wich you plane read from
    XML file. Actual include only one su"""
    def __init__(self):
        self.id = ""
        self.T42ObjectId = ""
        self.T42ObjectVersionId = ""
        self.name = ""
        self.version = ""
        self.creationDate = ""
        self.dOORSId = ""
        self.automation = ""
        self.testObjectCategory = ""
        self.testType = ""
        self.testDepth = ""
        self.specialFeature = ""
        self.testCaseEntries = list()
        self.description = ""




    def toString(x):

        "Create string for TestCaseEntries, be carefule with None value"

        values = list()
        "for each object in x.testCaseEntries, fill description in test case"
        for y in x.testCaseEntries:
            testData=""
            if y.text != None:
                if y.index == 1:
                    x.description = str(y.index) + " : " + y.text

                else:
                    testData = str(y.index - 1) + " : " + y.text
                    value = [x.id,x.T42ObjectVersionId, x.T42ObjectId, x.name,  x.version, x.creationDate, x.dOORSId,  x.automation, x.specialFeature, x.testType, x.testDepth, x.specialFeature, testData, x.description]
                    print(value)
                    values.append(value)


        print(values.__len__())
        return(values)


class TestCaseEntry:
    def __init__(self):
        self.type = ""
        self.index = ""
        self.text = ""

    def __str__(self):
        string = self.type, self.index, self.text
        return str

