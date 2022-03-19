from tkinter import *
from tkinter import ttk
import webbrowser

root = Tk()
root.geometry("650x410+340+10")


def cx():
    app2 = Tk()
    app2.geometry("650x410+340+10")
    lab = Label(app2, text="this is third page").pack()
    bot = Button(app2, text="third", command=mm).pack()


def fir():
    app = Tk()
    app.geometry("650x410+340+10")
    lab = Label(app, text="this is second page").pack()
    bot = Button(app, text="second", command=cx).pack()


btn = Button(root, text="first", command=fir).pack()

root.mainloop()
app.mainloop()
app2.mainloop()

# root = Tk()
# root.geometry("650x410+340+10")
# labelq = Label(root,  text='الخامس الاعدادي')
# labelq.place(x=50, y=10)


# def asss():
#     webbrowser.open(
#         'https://stackoverflow.com/search?page=2&tab=Relevance&q=how%20to%20combobox%20%20in%20tkinter')


# btn = Button(root, text="التربية الاسلامية", command=asss)
# btn.place(x=50, y=40)

# btn1 = Button(root, text="اللغة العربية", command=asss)
# btn1.place(x=50, y=80)

# btn2 = Button(root, text="الرياضيات", command=asss)
# btn2.place(x=50, y=120)

# btn3 = Button(root, text="اللغة الانكليزية ", command=asss)
# btn3.place(x=50, y=160)

# btn4 = Button(root, text="الكيمياء", command=asss)
# btn4.place(x=50, y=200)

# btn5 = Button(root, text="الفيزياء", command=asss)
# btn5.place(x=50, y=240)


# labelq = Label(root, text='الرابع الاعدادي')
# labelq.place(x=250, y=10)


# def asss():
#     webbrowser.open(
#         'https://stackoverflow.com/search?page=2&tab=Relevance&q=how%20to%20combobox%20%20in%20tkinter')


# btn = Button(root, text="التربية الاسلامية", command=asss)
# btn.place(x=250, y=40)

# btn1 = Button(root, text="اللغة العربية", command=asss)
# btn1.place(x=250, y=80)

# btn2 = Button(root, text="الرياضيات", command=asss)
# btn2.place(x=250, y=120)

# btn3 = Button(root, text="اللغة الانكليزية ", command=asss)
# btn3.place(x=250, y=160)

# btn4 = Button(root, text="الكيمياء", command=asss)
# btn4.place(x=250, y=200)

# btn5 = Button(root, text="الفيزياء", command=asss)
# btn5.place(x=250, y=240)

# root.mainloop()
