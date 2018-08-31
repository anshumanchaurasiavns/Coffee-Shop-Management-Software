import tkinter as tk 

root = tk.Tk() 
root.geometry("300x200") 
root.title("First Window")


def onclick(): 
    print("You clicked the button") 
    additional_window = tk.Toplevel()   #***********HERE*******
    additional_window.title("Additional Window")


button = tk.Button(root, text="click me", command=onclick) 
button.pack() 


root.mainloop() 