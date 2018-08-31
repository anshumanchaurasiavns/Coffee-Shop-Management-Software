from tkinter import *
import pymysql
from tkinter import messagebox

root=Tk()
f1=Frame(root,bg="white",width=300,height=299)
ent={}
did=0
obj={}
objs={}
number1=-1
number2=-1
root.minsize(width=966, height=666)
root.maxsize(width=967, height=667)

class Add:
    item1=0
    count=0
    inc = 0
    dict = {}
    lbc = 0

    def __init__(self):
        qty=0
        price=0.0
        title=""
        data={}
        self.item1= self.item1 + 1
        print(self.item1)

    def price(self,search):
        db = pymysql.connect("localhost", "root", "", "detail")
        cur = db.cursor()
        cur.execute("select price from items where title='"+search+"' ")
        res = cur.fetchone()[0]
        db.close()
        return res

    def imageclick(self,click):
        try:
            flag = "false"
            print(click,"Flag=",flag)
            if click in self.dict:
                flag="true"
                print("true title")
                temp = self.dict[click]
                temp1=""
                for i in temp.values():
                    for j in temp.keys():
                        self.dict[click][j]=self.dict[click][j]+1
                        temp1=j
                temp1.delete(0, END)
                result = self.price(click)
                temp = self.dict[click]
                for i in temp.values():
                    qty = i
                temp1.insert(END, click + "               " + str(result) + "Rs/Per Unit\n" + str(qty) + " Qty")
                print(self.dict)
            else:
                lb1 = Listbox(f1, height=2, width=50)
                print("false title")
                self.dict[click] = {lb1:1}
                print(self.dict)
                result=self.price(click)
                temp=self.dict[click]
                for i in temp.values():
                    qty=i
                lb1.insert(END,click+ "               "+str(result)+"Rs/Per Unit\n"+str(qty)+" Qty")
                lb1.pack()
                self.lbc += 1
        except Exception as e:
            print("Exception:",e)

    def images(self,img):
        title=img
        self.inc=self.inc+1
        try:
            val = "button" + str(self.inc)
            val1 = "image" + str(self.inc)
            print(val)
            print(val1)
            val = Button(f4, width=99, height=99,command=lambda: self.imageclick(title))
            img = "image\\" + img + ".png"
            print(img)
            val1=PhotoImage(file=img)
            val.config(image=val1)
            val.image = val1
        except TclError as e:
            print(e)
        val.pack(side=LEFT)

    def item(self):
        title = ""
        db = pymysql.connect("localhost", "root", "", "detail")
        cur = db.cursor()
        cur.execute("select count(*) from items")
        count = cur.fetchall()[0][0]
        print(count)
        #cur.fetchall()
        cur1 = db.cursor()
        cur1.execute("select * from items")
        for i in range(count):
            title=cur1.fetchone()[1]
            print(title)
            self.images(title)
#            print(i,"inside for loop")
        db.close()

def saver(name):
    re=ent["e1"].get()
    print(re)
    db = pymysql.connect("localhost", "root", "", "detail")
    cur = db.cursor()
    print(did)
    if(name=="reward"):
        cur.execute("update shop set reward='%s'"%(re)+"where id='%s'"%(did))
    elif(name=="note"):
        cur.execute("update shop set note='%s'" % (re) + "where id='%s'" % (did))
    #print(db.insert_id())
    db.close()

def rew():
    try:
        root2=Tk()
        root2.minsize(width=99, height=99)
        root2.maxsize(width=99, height=99)
        e1=Entry(root2)
        ent["e1"]=e1
        e1.pack()
        bu1=Button(root2,text="Save in Database",command=saver("reward"))
        bu1.pack()
    except Exception as e:
        print("Exception:",e)

def pay():
    try:
        global did
        loc = ""
        flag="false"
        Qty=0
        y = Add()
        payment = 0
        if len(y.dict) == 0:
            messagebox.showwarning("warning","Please Select Any Item")
        else:
            for i in y.dict.keys():
                price1=y.price(i)
                temp = y.dict[i]
                for j in temp.values():
                    qty = j
                    Qty=Qty+qty
                payment=payment+(price1*qty)
            for i in y.dict:
                if (flag == "false"):
                    loc=i
                    flag="true"
                if i not in loc:
                    loc=loc+","+i
            print(loc)
            db = pymysql.connect("localhost", "root", "", "detail")
            cur = db.cursor()
            cur.execute("insert into shop(id,item,price,qty,pay) values('%s','%s','%s','%s','%s')" % (0,loc,payment,Qty,"cash"))
            did=db.insert_id()
            db.close()
            l1=Label(f1, font=("Helvetica", 16),text="Rupees:"+str(payment))
            l1.pack()
    except Exception as e:
        print("Exception:", e)

def disc():
    try:
        x=Add()
        objs = {}
        temp={}
        for i in x.dict:
            print(i)
            temp[i] = x.dict[i].keys()
            print("temp ", temp)
            print("Keys", temp.keys())
            for j in temp[i]:
                items = j.curselection()
                if items:
                    print(items[0])
                    print("obj",j)
                    objs[i] = j
        print(objs)
        for i in objs:
    # objs[i].delete(0,END)
            objs[i].pack_forget()
            x.dict.pop(i, None)
    except Exception as e:
        print("Exception:",e)

def note():
    try:
        root3=Tk()
        root3.minsize(width=99, height=99)
        root3.maxsize(width=99, height=99)
        e2=Entry(root3)
        ent["e2"]=e2
        e2.pack()
        bu2=Button(root3,text="Save in Database",command=saver("note"))
        bu2.pack()
    except Exception as e:
        print("Exception:",e)

def quantity(lname):
    try:

        global number1
        global number2
        print(lname,"number")
        if(number1==-1):
            number1=lname
        else:
            number2=lname
    except Exception as e:
        print("Exception:",e)

def defqty():
    try:
        global number1
        global number2
        x=Add()
        objs = {}
        temp={}
        for i in x.dict:
            print(i)
            temp[i] = x.dict[i].keys()
            print("temp ", temp)
            print("Keys", temp.keys())
            for j in temp[i]:
                items = j.curselection()
                if items:
                    print(items[0])
                    print("obj",j)
                    objs[i] = j
        print("object",objs)
        for i in objs:
            local = str(number1) + str(number2)
            local = int(local)
            print("Quantity=", local)
            for i in objs.keys():
                click=i
            print("click",click)
            temp = x.dict[click]
            for i in temp.values():
                for j in temp.keys():
                    x.dict[click][j] = local
                    temp1 = j
        print(x.dict)
        temp1.delete(0, END)
        result = x.price(click)
        temp = x.dict[click]
        for i in temp.values():
            qty = i
        temp1.insert(END, click + "               " + str(result) + "Rs/Per Unit\n" + str(qty) + " Qty")
        number1=-1
        number2 = -1
    except Exception as e:
        print("Exception:",e)

f1.grid(row=0,column=0)
f2=Frame(root,bg="red")
f2.grid(row=0,column=1)
f3=Frame(root,bg="grey")
f3.grid(row=1,column=0)
b1=Button(f3,text="Rewards", width=10, height=2,command=rew)
b1.grid(row=0,column=0)
b2=Button(f3,text="Note", width=10, height=2,command=note)
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
f5=Frame(f3,bg="gray")
f5.grid(row=3,column=0,columnspan=3)
b8=Button(f5,text="Customer", width=12, height=2)
b8.grid(row=0,column=0,columnspan=3)
b9=Button(f5,text="1", width=4, height=2,command=lambda:quantity(1))
b9.grid(row=0,column=3)
b10=Button(f5,text="2", width=4, height=2,command=lambda:quantity(2))
b10.grid(row=0,column=4)
b11=Button(f5,text="3", width=4, height=2,command=lambda:quantity(3))
b11.grid(row=0,column=5)
b11=Button(f5,text="Qty", width=4, height=2,command=defqty)
b11.grid(row=0,column=6)
b12=Button(f5,text="Payment", width=12, height=7,command=pay)
b12.grid(row=1,column=0,columnspan=3,rowspan=3)
b13=Button(f5,text="4", width=4, height=2,command=lambda:quantity(4))
b13.grid(row=1,column=3)
b14=Button(f5,text="5", width=4, height=2,command=lambda:quantity(5))
b14.grid(row=1,column=4)
b15=Button(f5,text="6", width=4, height=2,command=lambda:quantity(6))
b15.grid(row=1,column=5)
b16=Button(f5,text="Disc", width=4, height=2,command=disc)
b16.grid(row=1,column=6)
b17=Button(f5,text="7", width=4, height=2,command=lambda:quantity(7))
b17.grid(row=2,column=3)
b18=Button(f5,text="8", width=4, height=2,command=lambda:quantity(8))
b18.grid(row=2,column=4)
b19=Button(f5,text="9", width=4, height=2,command=lambda:quantity(9))
b19.grid(row=2,column=5)
b20=Button(f5,text="Price", width=4, height=2)
b20.grid(row=2,column=6)
b21=Button(f5,text="+/-", width=4, height=2)
b21.grid(row=3,column=3)
b22=Button(f5,text="0", width=4, height=2,command=lambda:quantity(0))
b22.grid(row=3,column=4)
b23=Button(f5,text=".", width=4, height=2)
b23.grid(row=3,column=5)
b24=Button(f5,text="X", width=4, height=2)
b24.grid(row=3,column=6)

f4=Frame(root,bg="black")
f4.grid(row=1,column=1,ipady=1)
x=Add()
x.item()
root.mainloop()