
from tkinter import *
from listComp import *

names = ['hello1', 'hello2', 'hello3', 'hello4', 'hello5']

class TrialListbox(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.createWidgets()
        self.master.title('A Listbox Trial')
        self.master.iconname('tkpython')

    def createWidgets(self):
        self.makeList()
        self.makeButtons()

    def makeList(self):
        frame = Frame(self)
        frame.pack()
        scrollbar = Scrollbar(frame, orient=VERTICAL)
        self.listbox = Listbox(frame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
        for i in names:
            self.listbox.insert(END, i)

    def updateList(self):
        self.listbox.delete(0, END)
        for i in names:
            self.listbox.insert(END, i)

    def makeButtons(self):
        bframe = Frame(self)
        bframe.pack(side=BOTTOM)
        Button(bframe, text='Call Print', command=self.callPrint).pack(side=BOTTOM)
        Button(bframe, text='Quit', command=self.getOut).pack(side=BOTTOM)

    def callPrint(self):
        w1 = Toplevel()
        w1.window = ListComp(w1, self)
        w1.window.pack()

    def getOut(self):
        Frame.quit(self)

if __name__ == '__main__': TrialListbox().mainloop()

