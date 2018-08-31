from tkinter import *
import pymysql

dict={}

def imageclick(click):
    try:
        print(dict.keys())
        print(click)
        if click in dict:
            flag = "true"
            print("true title")
            dict[click] += 1
            print(dict)
            lb1.delete(0, END)
            lb1.insert(END, click + "               " + str("20") + "Rs/Per Unit\n" + str(dict[click]) + " Qty")
        else:
            print("false title")
            dict[click] = 1
            print(dict)
            lb1.insert(END, click + "               " + str("20") + "Rs/Per Unit\n" + str(dict[click]) + " Qty")
            lb1.pack()
    except Exception as e:
        print("Exception:", e)

root=Tk()
f1=Frame(root)
f1.pack()
lb1=Listbox(f1,width=120)
lb1.pack()
val = Button(root, width=99, height=99 ,command=lambda: imageclick("coffee"))
img = "C:\\Users\Anshuman\PycharmProjects\Imagebutton\image\coffee.png"
val1=PhotoImage(file=img)
val.config(image=val1)
val.image = val1
val.pack(side=LEFT)

root.mainloop()