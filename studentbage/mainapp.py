from tkinter import *
from tkinter import ttk
import webbrowser

firstwin = Tk()
firstwin.geometry("650x350")
firstwin.title("حقيبة الطالب")
firstwin.resizable(False, False)
firstwin.configure(background='#151D3B')


def secwind1():
    secwind = Tk()
    secwind.geometry("650x650")
    secwind.configure(background='#151D3B')
    # secwind.resizable(False, False)
    mlab = Label(secwind, text="مشاهدة الدروس الالكترونية",
                 bg='#151D3B', fg='white', font=(
                     "Tajawl", 14)).place(x=250, y=10)
    # الاول الابتادئي_______________________________
    wlb1 = Label(secwind, text=": الاول الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=530, y=45)
    wbtn1 = Button(secwind, text="التربية الاسلامية",
                   bg='#F0A500').place(x=530, y=75)

    wbtn2 = Button(secwind, text="   اللغة العربية   ",
                   bg='#F0A500').place(x=530, y=115)

    wbtn3 = Button(secwind, text="اللغة الانكليزية  ",
                   bg='#F0A500').place(x=530, y=155)

    wbtn4 = Button(secwind, text="   الرياضيات     ",
                   bg='#F0A500').place(x=530, y=195)

    wbtn5 = Button(secwind, text="       العلوم        ",
                   bg='#F0A500').place(x=530, y=235)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6
# الثاني الابتدائي_________________-
    wlb2 = Label(secwind, text=": الثاني الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=390, y=45)
    wbtn6 = Button(secwind, text="التربية الاسلامية",
                   bg='#F0A500').place(x=390, y=75)

    wbtn7 = Button(secwind, text="   اللغة العربية   ",
                   bg='#F0A500').place(x=390, y=115)

    wbtn8 = Button(secwind, text="  اللغة الانكليزية",
                   bg='#F0A500').place(x=390, y=155)

    wbtn9 = Button(secwind, text="    الرياضيات    ",
                   bg='#F0A500').place(x=390, y=195)

    wbtn10 = Button(secwind, text="        العلوم        ",
                    bg='#F0A500').place(x=390, y=235)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# الثالث الابتدائي__________________________________________________________
    wlb3 = Label(secwind, text=": الثالث الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=260, y=45)
    wbtn11 = Button(secwind, text="التربية الاسلامية",
                    bg='#F0A500').place(x=260, y=75)

    wbtn12 = Button(secwind, text="   اللغة العربية   ",
                    bg='#F0A500').place(x=260, y=115)

    wbtn13 = Button(secwind, text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=260, y=155)

    wbtn14 = Button(secwind, text="    الرياضيات    ",
                    bg='#F0A500').place(x=260, y=195)

    wbtn15 = Button(secwind, text="        العلوم        ",
                    bg='#F0A500').place(x=260, y=235)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6

    # الرابع الابتدائي _______________________________________________
    wlb4 = Label(secwind, text=": الرابع الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=520, y=310)
    wbtn16 = Button(secwind, text="التربية الاسلامية",
                    bg='#F0A500').place(x=530, y=350)
    wbtn17 = Button(secwind, text="   اللغة العربية   ",
                    bg='#F0A500').place(x=530, y=390)

    wbtn18 = Button(secwind, text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=530, y=430)

    wbtn19 = Button(secwind, text="    الرياضيات    ",
                    bg='#F0A500').place(x=530, y=470)

    wbtn20 = Button(secwind, text="        العلوم        ",
                    bg='#F0A500').place(x=530, y=510)
    wbtn39 = Button(secwind, text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=530, y=550)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^66

    # الخامس الابتدائي
    wlb5 = Label(secwind, text=": الخامس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=390, y=310)
    wbtn21 = Button(secwind, text="التربية الاسلامية",
                    bg='#F0A500').place(x=390, y=350)
    wbtn22 = Button(secwind, text="   اللغة العربية   ",
                    bg='#F0A500').place(x=390, y=390)

    wbtn23 = Button(secwind, text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=390, y=430)

    wbtn24 = Button(secwind, text="    الرياضيات    ",
                    bg='#F0A500').place(x=390, y=470)

    wbtn25 = Button(secwind, text="        العلوم        ",
                    bg='#F0A500').place(x=390, y=510)
    wbtn35 = Button(secwind, text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=390, y=550)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# السادس الابتدائي_____________________----
    wlb6 = Label(secwind, text=": السادس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=260, y=310)
    wbtn26 = Button(secwind, text="التربية الاسلامية",
                    bg='#F0A500').place(x=260, y=350)
    wbtn27 = Button(secwind, text="   اللغة العربية   ",
                    bg='#F0A500').place(x=260, y=390)

    wbtn28 = Button(secwind, text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=260, y=430)

    wbtn29 = Button(secwind, text="    الرياضيات    ",
                    bg='#F0A500').place(x=260, y=470)

    wbtn30 = Button(secwind, text="        العلوم        ",
                    bg='#F0A500').place(x=260, y=510)
    wbtn31 = Button(secwind, text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=260, y=550)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ دالة تحميل الكتب @@@@@@@@@@@@@@@@@@@@@@@@@


def thrwin():
    thrwin = Tk()
    thrwin.geometry("650x650")
    thrwin.configure(background='#151D3B')

    mlb = Label(thrwin, text=" تحميل الكتب الدراسية للمرحلة الابتدائية", bg='#151D3B',
                fg='white', font=("Tajawl", 14)).place(x=250, y=10)

    wlb1 = Label(thrwin, text=": الاول الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=530, y=45)

    wbtn1 = Button(thrwin, text="التربية الاسلامية",
                   bg='#F0A500').place(x=530, y=75)

    wbtn2 = Button(thrwin, text="   اللغة العربية   ",
                   bg='#F0A500').place(x=530, y=115)

    wbtn3 = Button(thrwin, text="اللغة الانكليزية  ",
                   bg='#F0A500').place(x=530, y=155)

    wbtn4 = Button(thrwin, text="   الرياضيات     ",
                   bg='#F0A500').place(x=530, y=195)

    wbtn5 = Button(thrwin, text="       العلوم        ",
                   bg='#F0A500').place(x=530, y=235)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6
# الثاني الابتدائي_________________-
    wlb2 = Label(thrwin, text=": الثاني الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=390, y=45)
    wbtn6 = Button(thrwin, text="التربية الاسلامية",
                   bg='#F0A500').place(x=390, y=75)

    wbtn7 = Button(thrwin, text="   اللغة العربية   ",
                   bg='#F0A500').place(x=390, y=115)

    wbtn8 = Button(thrwin, text="  اللغة الانكليزية",
                   bg='#F0A500').place(x=390, y=155)

    wbtn9 = Button(thrwin, text="    الرياضيات    ",
                   bg='#F0A500').place(x=390, y=195)

    wbtn10 = Button(thrwin, text="        العلوم        ",
                    bg='#F0A500').place(x=390, y=235)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# الثالث الابتدائي__________________________________________________________
    wlb3 = Label(thrwin, text=": الثالث الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=260, y=45)
    wbtn11 = Button(thrwin, text="التربية الاسلامية",
                    bg='#F0A500').place(x=260, y=75)

    wbtn12 = Button(thrwin, text="   اللغة العربية   ",
                    bg='#F0A500').place(x=260, y=115)

    wbtn13 = Button(thrwin, text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=260, y=155)

    wbtn14 = Button(thrwin, text="    الرياضيات    ",
                    bg='#F0A500').place(x=260, y=195)

    wbtn15 = Button(thrwin, text="        العلوم        ",
                    bg='#F0A500').place(x=260, y=235)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6

    # الرابع الابتدائي _______________________________________________
    wlb4 = Label(thrwin, text=": الرابع الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=520, y=310)
    wbtn16 = Button(thrwin, text="التربية الاسلامية",
                    bg='#F0A500').place(x=530, y=350)
    wbtn17 = Button(thrwin, text="   اللغة العربية   ",
                    bg='#F0A500').place(x=530, y=390)

    wbtn18 = Button(thrwin, text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=530, y=430)

    wbtn19 = Button(thrwin, text="    الرياضيات    ",
                    bg='#F0A500').place(x=530, y=470)

    wbtn20 = Button(thrwin, text="        العلوم        ",
                    bg='#F0A500').place(x=530, y=510)
    wbtn39 = Button(thrwin, text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=530, y=550)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^66

    # الخامس الابتدائي
    wlb5 = Label(thrwin, text=": الخامس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=390, y=310)
    wbtn21 = Button(thrwin, text="التربية الاسلامية",
                    bg='#F0A500').place(x=390, y=350)
    wbtn22 = Button(thrwin, text="   اللغة العربية   ",
                    bg='#F0A500').place(x=390, y=390)

    wbtn23 = Button(thrwin, text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=390, y=430)

    wbtn24 = Button(thrwin, text="    الرياضيات    ",
                    bg='#F0A500').place(x=390, y=470)

    wbtn25 = Button(thrwin, text="        العلوم        ",
                    bg='#F0A500').place(x=390, y=510)
    wbtn35 = Button(thrwin, text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=390, y=550)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# السادس الابتدائي_____________________----
    wlb6 = Label(thrwin, text=": السادس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=260, y=310)
    wbtn26 = Button(thrwin, text="التربية الاسلامية",
                    bg='#F0A500').place(x=260, y=350)
    wbtn27 = Button(thrwin, text="   اللغة العربية   ",
                    bg='#F0A500').place(x=260, y=390)

    wbtn28 = Button(thrwin, text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=260, y=430)

    wbtn29 = Button(thrwin, text="    الرياضيات    ",
                    bg='#F0A500').place(x=260, y=470)

    wbtn30 = Button(thrwin, text="        العلوم        ",
                    bg='#F0A500').place(x=260, y=510)
    wbtn31 = Button(thrwin, text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=260, y=550)

    # ****************************************** الشاشه الاولى *********************************
    # ليبل الاول
lab1 = Label(firstwin, text="مرحبا بك في تطبيق حقيبة الطالب", bg='#151D3B',  fg='#F0A500', font=("Tajawl", 20)).place(
    x=150, y=20)

# ليبل الثاني
mainlabel = Label(firstwin, text=": اختر مرحلتك الدراسية", bg='#151D3B',  fg='white', font=(
    "Tajawl", 18)).place(x=420, y=70)


lab2 = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18),  text=": المرحلة الابتدائية").place(x=350, y=120)

btn1 = Button(firstwin, command=thrwin, text="     تحميل الكتب     ",
              bg='#F0A500').place(x=40, y=120)
btn1 = Button(firstwin, command=secwind1, text="     مشاهدة الدروس الالكترونية     ", fg='white', bg='#ab1111').place(
    x=150, y=120)


lab3 = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18),  text="المرحلة المتوسطة").place(x=350, y=200)

btn1 = Button(firstwin, text="     تحميل الكتب     ",
              bg='#F0A500').place(x=40, y=200)
btn1 = Button(firstwin, text="     مشاهدة الدروس الالكترونية     ", fg='white', bg='#ab1111').place(
    x=150, y=200)


lab4 = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18),  text="المرحلة الاعدادية").place(x=350, y=280)


btn1 = Button(firstwin, text="     تحميل الكتب     ",
              bg='#F0A500').place(x=40, y=280)
btn1 = Button(firstwin, text="     مشاهدة الدروس الالكترونية     ", fg='white', bg='#ab1111').place(
    x=150, y=280)
# *********************************************************************************************


firstwin.mainloop()
secwind.mainloop()
thrwin.mainloop()
