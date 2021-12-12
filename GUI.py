
import TestCaseTREE as tc
import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "newproject"


class NewprojectWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(NewprojectWidget, self).__init__(master, **kw)
        self.labelframe = ttk.Labelframe(self)
        self.lbSourceFile = ttk.Entry(self.labelframe)
        self.txtPathSourceFile = tk.StringVar(value='/home/jan/Plocha/VývojSW/Python/Projekty/ImportTestcase/CS/testCS (kopie).xml')
        self.lbSourceFile.configure(exportselection='false', textvariable=self.txtPathSourceFile)
        _text_ = '/home/jan/Plocha/VývojSW/Python/Projekty/ImportTestcase/CS/testCS (kopie).xml'
        self.lbSourceFile.delete('0', 'end')
        self.lbSourceFile.insert('0', _text_)
        self.lbSourceFile.grid(column='2', row='1')
        self.lbOutputFile = ttk.Entry(self.labelframe)
        self.txtPathOutFile = tk.StringVar(value='')
        self.lbOutputFile.configure(textvariable=self.txtPathOutFile)
        self.lbOutputFile.grid(column='2', row='2')
        self.lbComponent = ttk.Entry(self.labelframe)
        self.txtComponent = tk.StringVar(value='')
        self.lbComponent.configure(font='TkMenuFont', textvariable=self.txtComponent)
        self.lbComponent.grid(column='2', row='3')
        self.label1 = ttk.Label(self.labelframe)
        self.label1.configure(background='#99de06', text='Importovane XML:')
        self.label1.grid(column='1', row='1', sticky='w')
        self.Z = ttk.Label(self.labelframe)
        self.Z.configure(background='#99de06', text='Vystupni soubor:')
        self.Z.grid(column='1', row='2', sticky='w')
        self.label3 = ttk.Label(self.labelframe)
        self.label3.configure(anchor='n', background='#99de06', font='TkMenuFont', text='Component:')
        self.label3.grid(column='1', row='3', sticky='w')
        self.label4 = ttk.Label(self.labelframe)
        self.label4.configure(background='#99de06', text='Priorita:')
        self.label4.grid(column='1', row='9', sticky='w')
        self.lbPriorita = ttk.Entry(self.labelframe)
        self.txtPriorita = tk.StringVar(value='')
        self.lbPriorita.configure(textvariable=self.txtPriorita)
        self.lbPriorita.grid(column='2', row='9')
        self.btRun = ttk.Button(self.labelframe)
        self.btRun.configure(cursor='arrow', text='Run')
        self.btRun.grid(column='1', row='10')
        self.btRun.configure(command=self.btRun)
        self.btClose = ttk.Button(self.labelframe)
        self.btClose.configure(cursor='arrow', text='Close')
        self.btClose.grid(column='2', row='10')
        self.btClose.configure(command=self.btClose)
        self.btClose.bind('<1>', self.callback, add='')
        self.labelframe.configure(height='500', labelanchor='n', text='Import do JIRA', width='400')
        self.labelframe.pack(side='left')

    def btRun(self):
        tc.parse("/home/jan/Plocha/VývojSW/Python/Projekty/ImportTestcase/CS/testCS (kopie).xml")
        print("Run skript...")
        pass

    def btClose(self):
        pass

    def callback(self, event=None):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    widget = NewprojectWidget(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()

