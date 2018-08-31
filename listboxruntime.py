from tkinter import *

root=Tk()
lbc=0
d={}

def click():
    d[store].delete(0, END)


#lb1 = "listbox" + str(lbc)
store = "coffee"
#print(lb1)
lb1 = Listbox(root, height=2, width=50)
print(lb1)
d[store]=lb1
#lb1.insert(END,"Here lb1")
d[store].insert(END,"Here obj")
b1=Button(root,text="Click",command=click)
d[store].pack()
b1.pack()
root.mainloop()