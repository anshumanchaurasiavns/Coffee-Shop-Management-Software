from tkinter import *
#import tkinter as ttk

def click():
    print("Inside click")
    text.delete(1.0, END)

root=Tk()
f1=Frame(root,bg="yellow")
f1.pack(side=LEFT)
text=Text(f1,width=99,height=2)
#text.insert(INSERT, "click here!                      ", "q")
print(text)
text.insert(END, "world\nunit 1")
#text.tag_config("n", background="yellow", foreground="red")
text.pack()
b1=Button(f1,text="Click",command=click)
b1.pack()
root.mainloop()