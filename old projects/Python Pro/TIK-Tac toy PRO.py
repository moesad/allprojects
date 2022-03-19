# Tik Tac Toy
# Mohaammed Sadiq     -B-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

root=Tk()
root.title('Tik-Tac toy') 
style= ttk.Style()
style.theme_use("classic")

active= 1
p1= []
p2= []

# ------Buttons--------
bt1= ttk.Button(root, text=" ")
bt1.grid(row= 0, column=0, sticky='snew', ipadx=40, ipady=40)
bt1.config(command= lambda: btclk(1), )

bt2= ttk.Button(root, text=" ")
bt2.grid(row= 0, column=1, sticky='snew', ipadx=40, ipady=40)
bt2.config(command= lambda: btclk(2))

bt3= ttk.Button(root, text=" ")
bt3.grid(row= 0, column=2, sticky='snew', ipadx=40, ipady=40)
bt3.config(command= lambda: btclk(3))

bt4= ttk.Button(root, text=" ")
bt4.grid(row= 1, column=0, sticky='snew', ipadx=40, ipady=40)
bt4.config(command= lambda: btclk(4))

bt5= ttk.Button(root, text=" ")
bt5.grid(row= 1, column=1, sticky='snew', ipadx=40, ipady=40)
bt5.config(command= lambda: btclk(5))

bt6= ttk.Button(root, text=" ")
bt6.grid(row= 1, column=2, sticky='snew', ipadx=40, ipady=40)
bt6.config(command= lambda: btclk(6))

bt7= ttk.Button(root, text=" ")
bt7.grid(row= 2, column=0, sticky='snew', ipadx=40, ipady=40)
bt7.config(command= lambda: btclk(7))

bt8= ttk.Button(root, text=" ")
bt8.grid(row= 2, column=1, sticky='snew', ipadx=40, ipady=40)
bt8.config(command= lambda: btclk(8))

bt9= ttk.Button(root, text=" ")
bt9.grid(row= 2, column=2, sticky='snew', ipadx=40, ipady=40)
bt9.config(command= lambda: btclk(9))

# --------win place---------------
def winch():
    winner = -1
# ---------p1------------
    if(1 in p1) and (2 in p1) and (3 in p1):
        winner = 1

    if(4 in p1) and (5 in p1) and (6 in p1):
        winner = 1 

    if(7 in p1) and (8 in p1) and (9 in p1):
        winner = 1        

    if(1 in p1) and (4 in p1) and (7 in p1):
        winner = 1 

    if(2 in p1) and (5 in p1) and (8 in p1):
        winner = 1

    if(3 in p1) and (6 in p1) and (9 in p1):
        winner = 1 

    if(1 in p1) and (5 in p1) and (9 in p1):
        winner = 1        

    if(3 in p1) and (5 in p1) and (7 in p1):
        winner = 1     
# ------------ p2 -----------
    if(1 in p2 )and (2 in p2) and (3 in p2):
        winner = 2

    if(4 in p2) and (5 in p2) and (6 in p2):
        winner = 2 

    if(7 in p2) and (8 in p2) and (9 in p2):
        winner = 2        

    if(1 in p2) and (4 in p2) and (7 in p2):
        winner =2 

    if(2 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if(3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if(1 in p2) and (5 in p2) and (9 in p2):
        winner = 2       

    if(3 in p2) and (5 in p2) and (7 in p2):
        winner = 2 
    if (winner ==1):
        messagebox.showinfo(title = " well done", message ='player 1 win' )

    elif (winner ==2):
        messagebox.showinfo(title=" well done", message ="player 2 win")    

# --------------buttons function-----------
def btclk(id):
    global active
    global p1
    global p2

    if (active == 1):
            chbtn(id, 'X')
            p1.append(id)
            root.title("player 2 turn")
            active = 2
            print('p1', p1)
            Autoplay()
    elif (active == 2):
            chbtn(id, 'O')
            p2.append(id)
            root.title("player 1 turn")
            active = 1
            print('p2', p2)

    winch()

# ----------------------------------------------------------

def chbtn(id, text):
    if (id ==1):
        bt1.config(text= text)    
        bt1.state(['disabled'])

        
    if (id ==2):
        bt2.config(text = text)    
        bt2.state(['disabled'])

        
    if (id ==3):
        bt3.config(text= text)    
        bt3.state(['disabled'])      

    if (id ==4):
        bt4.config(text= text)    
        bt4.state(['disabled'])

        
    if (id ==5):
        bt5.config(text= text)    
        bt5.state(['disabled'])

        
    if (id ==6):
        bt6.config(text= text)    
        bt6.state(['disabled'])  

    if (id ==7):
        bt7.config(text= text)    
        bt7.state(['disabled'])

        
    if (id ==8):
        bt8.config(text= text)    
        bt8.state(['disabled'])

        
    if (id ==9):
        bt9.config(text= text)    
        bt9.state(['disabled'])           

# ---------Autoplay code--------------

def Autoplay():
    global p1
    global p2
    emcell= []
    for cell in range (9):
        if ( not((cell+1 in p1) or (cell+1 in p2)) ):
            emcell.append(cell+1)
    rundindex= randint(0, len(emcell)-1)
    btclk(emcell[rundindex])        

root.mainloop()