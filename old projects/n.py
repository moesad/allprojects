from tkinter import *
from tkinter import ttk
import webbrowser
root = Tk()

root.title("moha")
root.geometry("650x410+340+10")

chos = [0, 1]
ch = ttk.Combobox(root, values=chos)
ch.pack()
a = ch.get()


def tj():
    webbrowser.open('google.com')


def open_cc():
    webbrowser.open('https://www.youtube.com/')


btn1 = Button(root, text='tk', command=tj).pack()
btn = Button(root, text="youtube", command=open_cc)
btn.pack()


mainloop()

# def selection(event):
#     webbrowser.open('https://www.youtube.com/')


# root = Tk()
# values = [1, 2, 3]
# combo_var = StringVar()
# combo = ttk.Combobox(root, values=values, textvariable=combo_var)
# combo.pack()
# combo.bind("<<ComboboxSelected>>",  selection)
# root.mainloop()
