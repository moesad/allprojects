from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# حل مشكة المسج !!!!!!!!!
activ= 1
p1= []
p2=[]

                                                            # note book !!!!!!!!!!!!!!!!!!!!!
root = Tk()
root.title("player 1 turn")

def winch():
    winner = -1

        # player 1
    if (1 in p1) and (2 in p1) and (3 in p1):
        winner = 1

    if (4 in p1) and (5 in p1) and (6 in p1):
        winner = 1

    if (7 in p1) and (8 in p1) and (9 in p1):
        winner = 1    

    if (1 in p1) and (4 in p1) and (7 in p1):
        winner = 1

    if (1 in p1) and (5 in p1) and (9 in p1):
        winner = 1

    if (2 in p1) and (5 in p1) and (8 in p1):
        winner = 1   

    if (3 in p1) and (6 in p1) and (9 in p1):
        winner = 1

    if (1 in p1) and (5 in p1) and (9 in p1):
        winner = 1

    if (3 in p1) and (5 in p1) and (7 in p1):
        winner = 1           

            # player 2

    if (1 in p2) and (2 in p2) and (3 in p2):
        winner = 2

    if (4 in p2) and (5 in p2) and (6 in p2):
        winner = 2

    if (7 in p2) and (8 in p2) and (9 in p2):
        winner = 2    

    if (1 in p2) and (4 in p2) and (7 in p2):
        winner = 2

    if (1 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if (2 in p2) and (5 in p2) and (8 in p2):
        winner = 2  

    if (3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if (1 in p2) and (5 in p2) and (9 in p2):
        winner = 2
# تاكد من الاعمدة + p2
    if (3 in p2) and (5 in p2) and (7 in p2):
        winner = 2  

    if (winner ==1):
        messagebox.showinfo(title = " well done", message ='player 1 win' )

    if (winner ==2):
        messagebox.showinfo(title=" well done", message ="player 2 win")

def btclk(id):
    global activ
    global p1            #check id
    global p2
    if (activ == 1):
        chnbtn(id, "X")
        p1.append(id)
        root.title("player 2 turn")
        activ =2
        print('p1', p1)

    elif (activ == 2):
        chnbtn(id, "O")
        p2.append(id)
        root.title("player 1 turn")
        activ = 1
        print('p2', p2)

    winch() # for show the winner


def chnbtn(id, text):   # in the NoteBook
    if (id ==1):
        b1.config(text= text)    
        b1.state(['disabled'])

        
    if (id ==2):
        b2.config(text= text)    
        b2.state(['disabled'])

        
    if (id ==3):
        b3.config(text= text)    
        b3.state(['disabled'])      # for make botton disabled

    if (id ==4):
        b4.config(text= text)    
        b4.state(['disabled'])

        
    if (id ==5):
        b5.config(text= text)    
        b5.state(['disabled'])

    if (id ==6):
        b6.config(text= text)    
        b6.state(['disabled'])  

    if (id ==7):
        b7.config(text= text)    
        b7.state(['disabled'])

        
    if (id ==8):
        b8.config(text= text)    
        b8.state(['disabled'])

        
    if (id ==9):
        b9.config(text= text)    
        b9.state(['disabled'])             

# make grid here: 
# searh what mran sticky

b1= ttk.Button(root, text= " ")
b1.grid(row=0 , column=0 , sticky="snew" , ipadx=40 , ipady= 40)
b1.config(command= lambda: btclk(1))

b2= ttk.Button(root, text= " ")
b2.grid(row=0 , column=1 , sticky="snew" , ipadx=40 , ipady= 40)
b2.config(command= lambda: btclk(2))

b3= ttk.Button(root, text= " ")
b3.grid(row=0 , column=2 , sticky="snew" , ipadx=40 , ipady= 40)
b3.config(command= lambda: btclk(3))

b4= ttk.Button(root, text= " ")
b4.grid(row=1 , column=0 , sticky="snew" , ipadx=40 , ipady= 40)
b4.config(command= lambda: btclk(4))

b5= ttk.Button(root, text= " ")
b5.grid(row=1 , column=1 , sticky="snew" , ipadx=40 , ipady= 40)
b5.config(command= lambda: btclk(5))

b6= ttk.Button(root, text= " ")
b6.grid(row=1 , column=2 , sticky="snew" , ipadx=40 , ipady= 40)  
b6.config(command= lambda: btclk(6))        # xعلى محور 

b7= ttk.Button(root, text= " ")
b7.grid(row=2 , column=0 , sticky="snew" , ipadx=40 , ipady= 40)
b7.config(command= lambda: btclk(7))

b8= ttk.Button(root, text= " ")
b8.grid(row=2 , column=1 , sticky="snew" , ipadx=40 , ipady= 40)
b8.config(command= lambda: btclk(8))

b9= ttk.Button(root, text= " ")
b9.grid(row=2 , column=2 , sticky="snew" , ipadx=40 , ipady= 40)
b9.config(command= lambda: btclk(9))
# remeber in notebook
root.mainloop()