from tkinter import *
from tkinter import ttk
import webbrowser


firstwin = Tk()
firstwin.geometry("650x400")
firstwin.title("حقيبة الطالب V1.2")
# firstwin.resizable(False, False)
firstwin.configure(background='#151D3B')


dlab = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18),  text="تحميل الدروس").place(x=360, y=342)
dbtn = Button(firstwin, text="                اظغط هنا لتحميل الدروس الالكترونية                ", fg='white', bg='#ab1111').place(
    x=45, y=350)
# ______________________________________________________


def secwind1():
    secwind = Tk()
    secwind.title('مشاهدة الدروس الالكترونية')
    secwind.geometry("650x650")
    secwind.configure(background='#151D3B')
    # secwind.resizable(False, False)
    mlab = Label(secwind, text="مشاهدة الدروس الالكترونية",
                 bg='#151D3B', fg='white', font=(
                     "Tajawl", 14)).place(x=250, y=10)
    # الاول الابتادئي_______________________________

    wlb1 = Label(secwind, text=": الاول الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=530, y=45)

    wbtn1 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=GSGJGgHPyPU&list=PLo81HqzE036oG7uZvSh2eYQSiYB_1UWgs'),  text="التربية الاسلامية",
                   bg='#F0A500').place(x=530, y=75)

    wbtn2 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=zLaTrZ81Eg4&list=PLo81HqzE036qoY2VkcmqI_5yHbuS_vSVv'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=530, y=115)

    wbtn3 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Bw9GIGkiwzo'), text="اللغة الانكليزية  ",
                   bg='#F0A500').place(x=530, y=155)

    wbtn4 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=pE3UhAkd1DU&list=PLNm6qUoPGFki8XXMYjA-joeQMWRGAa4QV'), text="   الرياضيات     ",
                   bg='#F0A500').place(x=530, y=195)

    wbtn5 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=4sZ2e3VAtaY&list=PLNm6qUoPGFkgyRKKEcPsbFp_cf-EE-hC8'), text="       العلوم        ",
                   bg='#F0A500').place(x=530, y=235)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6
# الثاني الابتدائي_________________-
    wlb2 = Label(secwind, text=": الثاني الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=390, y=45)

    wbtn6 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=BakLd6NyIOA&list=PLo81HqzE036og-tv1wDRMFAtxnHT4Q9rH'), text="التربية الاسلامية",
                   bg='#F0A500').place(x=390, y=75)

    wbtn7 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=g7GF-f93Jgw'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=390, y=115)

    wbtn8 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=W6H0lTz8TF0'), text="  اللغة الانكليزية",
                   bg='#F0A500').place(x=390, y=155)

    wbtn9 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=R373GhD1udo&list=PLNm6qUoPGFkjBiHJd3qHFPzRnsILiEKnW'), text="    الرياضيات    ",
                   bg='#F0A500').place(x=390, y=195)

    wbtn10 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=LABSz08lOis'), text="        العلوم        ",
                    bg='#F0A500').place(x=390, y=235)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# الثالث الابتدائي__________________________________________________________
    wlb3 = Label(secwind, text=": الثالث الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=260, y=45)

    wbtn11 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Q2VxQwGTLcM'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=260, y=75)

    wbtn12 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=CfdgNDOdVsU&list=PLNm6qUoPGFkgDxRuMtjYoWiAJz09FyxHs'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=260, y=115)

    wbtn13 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=HtkNletiy1U&list=PLNm6qUoPGFkiZawQSohdnrsGuYRNfN82p'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=260, y=155)

    wbtn14 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=jKuHnEq4hsQ'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=260, y=195)

    wbtn15 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=R0XR_zoR0ow&list=PLNm6qUoPGFki1qQPBoGVlRZwv7_dy-wzB'), text="        العلوم        ",
                    bg='#F0A500').place(x=260, y=235)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6

    # الرابع الابتدائي _______________________________________________
    wlb4 = Label(secwind, text=": الرابع الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=520, y=310)

    wbtn16 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=ok-E5M3IXY0'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=530, y=350)

    wbtn17 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=bIQ2YQiVH4c&list=PLo81HqzE036oTcY-u1cl6yZ5-p7aKhiCX'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=530, y=390)

    wbtn18 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=7YhyVp-TBb4'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=530, y=430)

    wbtn19 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=LdTQdBR688w'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=530, y=470)

    wbtn20 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=TMYr9lQ6gs0'), text="        العلوم        ",
                    bg='#F0A500').place(x=530, y=510)

    wbtn39 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=04Lav9GUQuc'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=530, y=550)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^66

    # الخامس الابتدائي
    wlb5 = Label(secwind, text=": الخامس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=390, y=310)

    wbtn21 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=xG0XkxhRZu4'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=390, y=350)

    wbtn22 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Ley_tTCTwpo&list=PLo81HqzE036q4Tifj_nXhzdYFIWlYZm5S'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=390, y=390)

    wbtn23 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=nx2-xp1UG4c'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=390, y=430)

    wbtn24 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=65oTDBzmqtI'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=390, y=470)

    wbtn25 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=t5zV7Ajm_v0'), text="        العلوم        ",
                    bg='#F0A500').place(x=390, y=510)

    wbtn35 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=psvAeYxt8cc'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=390, y=550)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# السادس الابتدائي_____________________----
    wlb6 = Label(secwind, text=": السادس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=260, y=310)

    wbtn26 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=CRUO0ddlk-Y'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=260, y=350)

    wbtn27 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=G-3rGLlJOr8'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=260, y=390)

    wbtn28 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=R3dFbe2CdKc'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=260, y=430)

    wbtn29 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=vwfMqzVVLPE'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=260, y=470)

    wbtn30 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=cGg2AnB_no0'), text="        العلوم        ",
                    bg='#F0A500').place(x=260, y=510)

    wbtn31 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=12JrIwc-KNA'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=260, y=550)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ دالة تحميل الكتب @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def thrwin():
    thrwin = Tk()
    thrwin.geometry("650x650")
    thrwin.configure(background='#151D3B')
    mlb = Label(thrwin, text=" تحميل الكتب الدراسية للمرحلة الابتدائية", bg='#151D3B',
                fg='white', font=("Tajawl", 14)).place(x=250, y=10)

    wlb1 = Label(thrwin,  text=": الاول الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=530, y=45)

    wbtn1 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1_Q0l-a3TVyYG1ggy70O19s6umHMA5h0y/view?usp=sharing'), text="التربية الاسلامية",
                   bg='#F0A500').place(x=530, y=75)

    wbtn2 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1HgBx7_0Y3CwnthrEyI3rlZz2bsMhrLZp/view?usp=sharing'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=530, y=115)

    wbtn3 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1NZkhlUY-_U6-DO_DMpxt28uiWljY-jMv/view?usp=sharing'), text="اللغة الانكليزية  ",
                   bg='#F0A500').place(x=530, y=155)

    wbtn4 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1fhxxBNoCxUi_gj0t4-gzsDO3h9SxSMt1/view?usp=sharing'), text="   الرياضيات     ",
                   bg='#F0A500').place(x=530, y=195)

    wbtn5 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1NxlZA83DUw57RgwpbJQkZE_Q3PgNzVu5/view?usp=sharing'), text="       العلوم        ",
                   bg='#F0A500').place(x=530, y=235)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6
# الثاني الابتدائي_________________-
    wlb2 = Label(thrwin, text=": الثاني الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=390, y=45)

    wbtn6 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1W8_edy6ynr1ee6jk4buQLFzQ8_CTfN1N/view?usp=sharing'), text="التربية الاسلامية",
                   bg='#F0A500').place(x=390, y=75)

    wbtn7 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1XK7m2TwffuQuC2VebRCkHTL_MiLAbTiP/view?usp=sharing'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=390, y=115)

    wbtn8 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1ilrnp_zDnPL6Dq6x3_tSsrQhuiikImgj/view?usp=sharing'), text="  اللغة الانكليزية",
                   bg='#F0A500').place(x=390, y=155)

    wbtn9 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1zuNU47FFmCEOgaK4kfl93WUEsjzZwvfb/view?usp=sharing'), text="    الرياضيات    ",
                   bg='#F0A500').place(x=390, y=195)

    wbtn10 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1mvBOalgJbjXROmhi6kRQPkbqOU0Pv08b/view?usp=sharing'), text="        العلوم        ",
                    bg='#F0A500').place(x=390, y=235)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# الثالث الابتدائي__________________________________________________________
    wlb3 = Label(thrwin, text=": الثالث الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=260, y=45)

    wbtn11 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/12uxDqQIIsdvMmH6kLThZ8TFm_vPas20n/view?usp=sharing'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=260, y=75)

    wbtn12 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/19r7cizG9NGyydmEVWvVPLR2EllgTv7Cz/view?usp=sharing'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=260, y=115)

    wbtn13 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1EGejLGTHrMt9NrwCwMMIQpBwuZqLBUOs/view?usp=sharing'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=260, y=155)

    wbtn14 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1bwMnMTQVhB-_SosCmmd845O04K3RJU3W/view?usp=sharing'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=260, y=195)

    wbtn15 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/17sewQhuOLP1Zbc4Sxi6vIMqlqm3GY3q6/view?usp=sharing'), text="        العلوم        ",
                    bg='#F0A500').place(x=260, y=235)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6

    # الرابع الابتدائي _______________________________________________
    wlb4 = Label(thrwin, text=": الرابع الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=520, y=310)

    wbtn16 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1YidDMFcuBBcsK8RFo15JGFHhMrxhRDqB/view?usp=sharing'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=530, y=350)

    wbtn17 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1t--2H88AA8Fi-y4ZlISco6sd0zK2ss1l/view?usp=sharing'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=530, y=390)

    wbtn18 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/11HIB888QCKra8OwG8582K59xcLdXOhyV/view?usp=sharing'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=530, y=430)

    wbtn19 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1D75FfN2nbtaueommkxPqMUb6Y5X5YDJR/view?usp=sharing'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=530, y=470)

    wbtn20 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1JwWOgdulWb9ZRaMNXiI2dOMl8yS_8R2Z/view?usp=sharing'), text="        العلوم        ",
                    bg='#F0A500').place(x=530, y=510)

    wbtn39 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/14mQvYtomtWCoJIWllarUm-ZdB5MYQSAZ/view?usp=sharing'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=530, y=550)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^66

    # الخامس الابتدائي
    wlb5 = Label(thrwin, text=": الخامس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=390, y=310)

    wbtn21 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1fGBq0lZ4yQnucPasuphkTWyEJI72pRkv/view'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=390, y=350)

    wbtn22 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1K4IkgHoFIcT13K_G5bKM6SpM3HlLJRRi/view?usp=sharing'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=390, y=390)

    wbtn23 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1FbRsq9cJ-H1N_YmWfsYmZAgh5NwPWmGd/view?usp=sharing'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=390, y=430)

    wbtn24 = Button(thrwin, command=lambda: webbrowser.open('https://up.mlazemna.com/bk5pmth/'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=390, y=470)

    wbtn25 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/15eQe92487aMZVCRNcyPKGNGHik2B7VgE/view?usp=sharing'), text="        العلوم        ",
                    bg='#F0A500').place(x=390, y=510)

    wbtn35 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1or9dw1q67XWCiQRlhCkbld0JWfntHd-U/view?usp=sharing'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=390, y=550)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# السادس الابتدائي_____________________----
    wlb6 = Label(thrwin, text=": السادس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13)).place(x=260, y=310)

    wbtn26 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/14upGVPdPoRKN8iXC6Uf6bPrCHd3MiRNe/view?usp=drivesdk'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=260, y=350)

    wbtn27 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1N3WRxbiWMOjNJHnRIlRBUxP-Z062uKz6/view?usp=drivesdk'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=260, y=390)

    wbtn28 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1lEqZaU4RCx_2IGGltIGAaITTs9yADDR0/view?usp=drivesdk'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=260, y=430)

    wbtn29 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1PAgYLsuOjWEYj0U-k87enYk8_CX8L4CL/view?usp=drivesdk'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=260, y=470)

    wbtn30 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1F2ZtcFwuau3J8E3fyFpBdiz_yTZ8H_Jw/view?usp=drivesdk'), text="        العلوم        ",
                    bg='#F0A500').place(x=260, y=510)

    wbtn31 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1s1Dnv2VhVEyuotryBXBlI8qe45XuxWmt/view?usp=drivesdk'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=260, y=550)


# @@@@@@@@@@@@@@@@@@@@@ دوال المرحلة المتوسطة @@@@@@@@@@@@@@@@@@@@@@@@

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
