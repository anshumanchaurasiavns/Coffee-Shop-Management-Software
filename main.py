from tkinter import *

import sqlite3
import time
from tkinter import messagebox
import datetime
import re
import os
from sqlite3 import *

conn=sqlite3.connect('shop.db')
cur=conn.cursor()
try:
    cur.execute("select * FROM detail")
    print("try")
except Exception as e:
    print(e,"except")
    cur.execute("create table detail(id int,title varchar(20),price int,qty int)")
    result = cur.execute("select * FROM detail")
    print("Successfully Created Table")
cur.close()
conn.close()

root=Tk()
f1=Frame(root,bg="white",  width=300, height=200)

class add:
    item=0
    def __init__(self):
        qty=0
        price=0.0
        title=""
        data={}
    def list(self,qty,price,title):
        for k in data.keys():
            if(k=="title"):
                data["title"]["qty"]+=1





l1=Label(f1,text="",bg="black", font=("Arial", 34,"bold"),fg="white",anchor=W, justify=LEFT)
l1.pack()
f1.grid(row=0,column=0)
f2=Frame(root,bg="red",  width=300, height=100)
f2.grid(row=0,column=1)
f3=Frame(root,bg="grey",  width=300, height=200)
f3.grid(row=1,column=0)
b1=Button(f3,text="Rewards", width=10, height=2)
b1.grid(row=0,column=0)
b2=Button(f3,text="Note", width=10, height=2)
b2.grid(row=0,column=1)
b3=Button(f3,text="Transfer", width=10, height=2)
b3.grid(row=0,column=2)
b4=Button(f3,text="Guests", width=10, height=2)
b4.grid(row=1,column=0)
b5=Button(f3,text="Bill", width=10, height=2)
b5.grid(row=1,column=1)
b6=Button(f3,text="Split", width=10, height=2)
b6.grid(row=1,column=2)
b7=Button(f3,text="Order", width=33, height=2)
b7.grid(row=2,column=0,columnspan=3)
f5=Frame(f3,bg="green")
f5.grid(row=3,column=0,columnspan=3)
b8=Button(f5,text="Customer", width=12, height=2)
b8.grid(row=0,column=0,columnspan=3)
b9=Button(f5,text="1", width=4, height=2)
b9.grid(row=0,column=3)
b10=Button(f5,text="2", width=4, height=2)
b10.grid(row=0,column=4)
b11=Button(f5,text="3", width=4, height=2)
b11.grid(row=0,column=5)
b11=Button(f5,text="Qty", width=4, height=2)
b11.grid(row=0,column=6)
b12=Button(f5,text="Payment", width=12, height=7)
b12.grid(row=1,column=0,columnspan=3,rowspan=3)
b13=Button(f5,text="4", width=4, height=2)
b13.grid(row=1,column=3)
b14=Button(f5,text="5", width=4, height=2)
b14.grid(row=1,column=4)
b15=Button(f5,text="6", width=4, height=2)
b15.grid(row=1,column=5)
b16=Button(f5,text="Disc", width=4, height=2)
b16.grid(row=1,column=6)
b17=Button(f5,text="7", width=4, height=2)
b17.grid(row=2,column=3)
b18=Button(f5,text="8", width=4, height=2)
b18.grid(row=2,column=4)
b19=Button(f5,text="9", width=4, height=2)
b19.grid(row=2,column=5)
b20=Button(f5,text="Price", width=4, height=2)
b20.grid(row=2,column=6)
b21=Button(f5,text="+/-", width=4, height=2)
b21.grid(row=3,column=3)
b22=Button(f5,text="0", width=4, height=2)
b22.grid(row=3,column=4)
b23=Button(f5,text=".", width=4, height=2)
b23.grid(row=3,column=5)
b24=Button(f5,text="X", width=4, height=2)
b24.grid(row=3,column=6)

f4=Frame(root,bg="black",  width=300, height=200)
f4.grid(row=1,column=1,ipady=1)
root.mainloop()