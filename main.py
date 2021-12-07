# This is a sample Python script.
import tkinter
import xml.sax
import xml.etree.ElementTree as ET
from pathlib import Path
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from TestCaseSAX import TestCaseObject
import TestCaseSAX
import TestCaseTREE as tree
import GUI


def parseSAX():
    parser = xml.sax.make_parser()
    Handler = TestCaseSAX.TestCaseHandler()
    parser.setContentHandler(Handler)
    parser.parse(open("/home/jan/Plocha/VývojSW/Python/Projekty/ImportTestcase/CS/testCS.xml","r"))



if __name__ == '__main__':
    path = "/home/jan/Plocha/VývojSW/Python/Projekty/ImportTestcase/CS/testCS (kopie).xml"
    tc = tree.parse(path)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
