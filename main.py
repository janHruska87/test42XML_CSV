# This is a sample Python script.
import datetime
from datetime import datetime
import pathlib
import tkinter as tk
import tkinter.ttk as ttk

from pygubu.widgets.pathchooserinput import PathChooserInput

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import SQLiteAPI
import TestCaseTREE as tc

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "newproject"


class GuixmlimporterApp:
    def __init__(self, master=None):
        # build ui
        self.frame1 = ttk.Frame(master)
        self.labelframe = ttk.Labelframe(self.frame1)
        self.lbComponent = ttk.Entry(self.labelframe)
        self.txtComponent = tk.StringVar(value='')
        self.lbComponent.configure(font='TkMenuFont', textvariable=self.txtComponent)
        self.lbComponent.grid(column='2', row='3')
        self.label1 = ttk.Label(self.labelframe)
        self.label1.configure(background='#99de06', text='Importovane XML:')
        self.label1.grid(column='1', row='1', sticky='w')
        self.Z = ttk.Label(self.labelframe)
        self.Z.configure(background='#99de06', compound='bottom', text='Vystupni adresar:')
        self.Z.grid(column='1', row='2', sticky='w')
        self.label3 = ttk.Label(self.labelframe)
        self.label3.configure(anchor='n', background='#99de06', font='TkMenuFont', text='Component:')
        self.label3.grid(column='1', row='3', sticky='w')
        self.label4 = ttk.Label(self.labelframe)
        self.label4.configure(background='#99de06', text='Priorita:')
        self.label4.grid(column='1', row='9', sticky='w')
        self.lbPriorita = ttk.Entry(self.labelframe)
        self.txtPriorita = tk.StringVar(value='A')
        self.lbPriorita.configure(textvariable=self.txtPriorita)
        self.lbPriorita.grid(column='2', row='9')
        self.btRun = ttk.Button(self.labelframe)
        self.btRun.configure(cursor='arrow', text='Run')
        self.btRun.grid(column='1', row='10')
        self.btRun.configure(command=self.clickBtRun)
        self.btClose = ttk.Button(self.labelframe)
        self.btClose.configure(cursor='arrow', text='Close')
        self.btClose.grid(column='2', row='10')
        self.btClose.configure(command=self.clickBtClose)
        self.btClose.bind('<1>', self.callback, add='')
        self.pathchooserInputXML = PathChooserInput(self.labelframe)
        self.pathchooserInputXML.configure(mustexist='true', title='Vyberte XML', type='file')
        self.pathchooserInputXML.grid(column='2', row='1')
        self.pathchooserOutputDir = PathChooserInput(self.labelframe)
        self.pathchooserOutputDir.configure(mustexist='true', title='Vyberte vystupni adresar', type='directory')
        self.pathchooserOutputDir.grid(column='2', row='2')
        self.text1 = tk.Text(self.labelframe)
        self.text1.configure(height='10', width='50')
        self.text1.grid(column='1', columnspan='2', row='12', rowspan='1')
        self.pathchooserDB = PathChooserInput(self.labelframe)
        self.pathchooserDB.configure(mustexist='true', title='Vyberte DB', type='file')
        self.pathchooserDB.grid(column='2', row='13')
        self.label2 = ttk.Label(self.labelframe)
        self.label2.configure(text='Vyber SQLiteDB')
        self.label2.grid(column='1', row='13')
        self.btTestConnection = ttk.Button(self.labelframe)
        self.btTestConnection.configure(text='Test connection')
        self.btTestConnection.grid(column='2', row='14')
        self.btTestConnection.configure(command=self.clickBtTestConnection)
        self.labelframe.configure(height='500', labelanchor='n', text='Import do JIRA', width='400')
        self.labelframe.pack(side='left')
        self.frame1.configure(height='200', width='200')
        self.frame1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame1

    def run(self):
        self.mainwindow.mainloop()

    def clickBtRun(self):
        "Doplneni komponenty a priority do testCase, predpoklada se ze komponenta odpovida nazvu sluzby"
        componenta = self.txtComponent.get()
        priorita = self.txtPriorita.get()
        print("Komponenta je:",componenta, " Priorita je:", priorita )
        "Volani samotne funkce spoustejici nacteni souboru XML a prevod do CSV"
        tc.parse(self.pathchooserInputXML.cget("path"),self.pathchooserOutputDir.cget("path"),componenta,priorita)
        pass

    def clickBtClose(self):
        root.destroy()
        pass

    def callback(self, event=None):
        pass

    def clickBtTestConnection(self):
        """header = [("id","PRIMARY KEY"),("T42ObjectVersionId","TEXT"), ("T42ObjectId", "TEXT"), ("name","TEXT"),  ("version","INTEGER"), ("creationDate","DATETIME"), ("dOORSId","INTEGER"),  "automation", "specialFeature", "testType", "testDepth", "specialFeature", "testData", "description"]"""
        header = [("id", "INTEGER PRIMARY KEY"), ("T42ObjectVersionId", "TEXT"), ("T42ObjectId", "TEXT"), ("name", "TEXT"),("version", "INTEGER"), ("creationDate", "DATETIME")]
        tableName = datetime.now().strftime("%Y_%m_%d_%H_%M") + "_data"
        SQLiteAPI.db.createTable(self, self.pathchooserDB.cget("path"),tableName,header)
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = GuixmlimporterApp(root)
    app.run()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
