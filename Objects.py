
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



    def toString(x):
        "Create sorted list object from input object"
        sortedX = list()
        c = 1
        for record in x.testCaseEntries:
            if record.index == c:
                sortedX.append(record)
                c = c + 1
            else:
                pass

        "Create string for TestCaseEntries, be carefule with None value"
        outString = ""
        for entry in sortedX:
            if entry.index != None:
                outString = outString + str(entry.index) + " - "
            if entry.type != None:
                outString = outString + entry.type + " - "
            if entry.text != None:
                outString = outString + entry.text + " - "
        "Final string which is append to output row (Values)"
        outString = outString + "\n"

        "Create string for basic TestCase parametrs"
        values = [x.id, x.name, x.creationDate, x.dOORSId, x.automation, x.specialFeature, x.testDepth, x.testType,
                  x.T42ObjectVersionId, x.T42ObjectId, outString]
        "print(values)"
        return values

class TestCaseEntry:
    def __init__(self):
        self.type = ""
        self.index = ""
        self.text = ""

    def __str__(self):
        string = self.type, self.index, self.text
        return str

