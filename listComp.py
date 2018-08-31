
from tkinter import *
from list import *

class ListComp(Frame):
    def __init__(self, parent=None, listBox=None):
        Frame.__init__(self, parent)
        self.trialListbox = listBox
        self.w1 = parent
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        bframe = Frame(self)
        bframe.pack()
        Button(bframe, text='Print', command=self.Iprint).pack(side=LEFT)
        Button(bframe, text='Quit', command=self.Iquit).pack(side=LEFT)
        Button(bframe, text='Add', command=self.Iadd).pack(side=LEFT)
        Button(bframe, text='Delete', command=self.Idel).pack(side=LEFT)

    def Iprint(self):
        if self.trialListbox != None:
            item = self.trialListbox.listbox.curselection()
            member = self.trialListbox.listbox.get(item)
            print('Term: ' + member)

    def Iquit(self):
        self.w1.destroy()

    def Iadd(self):
        names.append('hello')
        self.trialListbox.updateList()

    def Idel(self):
        item = self.trialListbox.listbox.curselection()
        member = self.trialListbox.listbox.get(item)
        names.remove(member)
        self.trialListbox.updateList()
