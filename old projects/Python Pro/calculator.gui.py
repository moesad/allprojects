from tkinter import *
from tkinter import ttk


root=Tk()

ex = ""
input_text = StringVar()



enter = ttk.Entry(root, width= 40, textvariable=input_text). pack()

frame= ttk.Frame(root)
frame.config(width=200, height=200, relief=RIDGE)
frame.pack()

def btclk(id):
    global ex
    ex += str(id)
    input_text.set(ex)

def clear():
     global ex
     ex = ""
     input_text.set(ex)

def findReslt():
    global ex 
    resut = str(eval(ex))
    input_text.set(resut)
    ex = ""


b1= ttk.Button(frame, text="1", command= lambda: btclk(1)).grid(row=0, column=0, padx=10, pady=10)
b2= ttk.Button(frame, text="2", command= lambda: btclk(2)).grid(row=0, column=1, padx=10, pady=10)
b3= ttk.Button(frame, text="3", command= lambda: btclk(3)).grid(row=0, column=2, padx=10, pady=10)
b4= ttk.Button(frame, text="+", command= lambda: btclk("+")).grid(row=0, column=3, padx=10, pady=10)

b5= ttk.Button(frame, text="4", command= lambda: btclk(4)).grid(row=1, column=0, padx=10, pady=10)
b6= ttk.Button(frame, text="5", command= lambda: btclk(5)).grid(row=1, column=1, padx=10, pady=10)
b7= ttk.Button(frame, text="6", command= lambda: btclk(6)).grid(row=1, column=2, padx=10, pady=10)
b8= ttk.Button(frame, text="-", command= lambda: btclk("-")).grid(row=1, column=3, padx=10, pady=10)

b7= ttk.Button(frame, text="7", command= lambda: btclk(7)).grid(row=2, column=0, padx=10, pady=10)
b8= ttk.Button(frame, text="8", command= lambda: btclk(8)).grid(row=2, column=1, padx=10, pady=10)
b9= ttk.Button(frame, text="9", command= lambda: btclk(9)).grid(row=2, column=2, padx=10, pady=10)
b10= ttk.Button(frame, text="*", command= lambda: btclk("*")).grid(row=2, column=3, padx=10, pady=10)

b1= ttk.Button(frame, text="0", command= lambda: btclk(0)).grid(row=3, column=0, padx=10, pady=10)
b2= ttk.Button(frame, text="C", command= lambda: clear()).grid(row=3, column=1, padx=10, pady=10)
b3= ttk.Button(frame, text=".", command= lambda: btclk(".")).grid(row=3, column=2, padx=10, pady=10)
b4= ttk.Button(frame, text="=", command= lambda: findReslt()).grid(row=3, column=3, padx=10, pady=10)




root.mainloop()