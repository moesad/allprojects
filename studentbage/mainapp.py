from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import filedialog


# ==== main win =====
firstwin = Tk()
firstwin.geometry("650x480")
firstwin.title("حقيبة الطالب V1.2")
firstwin.resizable(False, False)
firstwin.configure(background='#151D3B')


# ================================================================

def secwind1():
    secwind = Tk()
    secwind.title('مشاهدة الدروس الالكترونية')
    secwind.geometry("480x600")
    secwind.configure(background='#151D3B')
    secwind.resizable(False, False)
    mlab = Label(secwind, text="مشاهدة الدروس الالكترونية",
                 bg='#151D3B', fg='white', font=(
                     "Tajawl", 14)).place(x=150, y=10)

# ==================== الاول الابتدائي ================================

    wlb1 = Label(secwind, text=": الاول الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=360, y=45)

    wbtn1 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=GSGJGgHPyPU&list=PLo81HqzE036oG7uZvSh2eYQSiYB_1UWgs'),  text="التربية الاسلامية",
                   bg='#F0A500').place(x=360, y=75)

    wbtn2 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=zLaTrZ81Eg4&list=PLo81HqzE036qoY2VkcmqI_5yHbuS_vSVv'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=360, y=115)

    wbtn3 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Bw9GIGkiwzo'), text="اللغة الانكليزية  ",
                   bg='#F0A500').place(x=360, y=155)

    wbtn4 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=pE3UhAkd1DU&list=PLNm6qUoPGFki8XXMYjA-joeQMWRGAa4QV'), text="   الرياضيات     ",
                   bg='#F0A500').place(x=360, y=195)

    wbtn5 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=4sZ2e3VAtaY&list=PLNm6qUoPGFkgyRKKEcPsbFp_cf-EE-hC8'), text="       العلوم        ",
                   bg='#F0A500').place(x=360, y=235)
# ===================================================================

#  ====================== الثاني الابتدائي ==========================
    wlb2 = Label(secwind, text=": الثاني الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=200, y=45)

    wbtn6 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=BakLd6NyIOA&list=PLo81HqzE036og-tv1wDRMFAtxnHT4Q9rH'), text="التربية الاسلامية",
                   bg='#F0A500').place(x=200, y=75)

    wbtn7 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=g7GF-f93Jgw'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=200, y=115)

    wbtn8 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=W6H0lTz8TF0'), text="  اللغة الانكليزية",
                   bg='#F0A500').place(x=200, y=155)

    wbtn9 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=R373GhD1udo&list=PLNm6qUoPGFkjBiHJd3qHFPzRnsILiEKnW'), text="    الرياضيات    ",
                   bg='#F0A500').place(x=200, y=195)

    wbtn10 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=LABSz08lOis'), text="        العلوم        ",
                    bg='#F0A500').place(x=200, y=235)
# ===========================================================================

# ==================== الثالث الابتدائي =====================================
    wlb3 = Label(secwind, text=": الثالث الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=32, y=45)

    wbtn11 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Q2VxQwGTLcM'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=40, y=75)

    wbtn12 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=CfdgNDOdVsU&list=PLNm6qUoPGFkgDxRuMtjYoWiAJz09FyxHs'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=40, y=115)

    wbtn13 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=HtkNletiy1U&list=PLNm6qUoPGFkiZawQSohdnrsGuYRNfN82p'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=40, y=155)

    wbtn14 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=jKuHnEq4hsQ'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=40, y=195)

    wbtn15 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=R0XR_zoR0ow&list=PLNm6qUoPGFki1qQPBoGVlRZwv7_dy-wzB'), text="        العلوم        ",
                    bg='#F0A500').place(x=40, y=235)
# ========================================================

#  ============================ الرابع الابتدائي =========
    wlb4 = Label(secwind, text=": الرابع الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=360, y=310)

    wbtn16 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=ok-E5M3IXY0'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=360, y=350)

    wbtn17 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=bIQ2YQiVH4c&list=PLo81HqzE036oTcY-u1cl6yZ5-p7aKhiCX'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=360, y=390)

    wbtn18 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=7YhyVp-TBb4'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=360, y=430)

    wbtn19 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=LdTQdBR688w'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=360, y=470)

    wbtn20 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=TMYr9lQ6gs0'), text="        العلوم        ",
                    bg='#F0A500').place(x=360, y=510)

    wbtn39 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=04Lav9GUQuc'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=360, y=550)
    # ========================================================

    # =========================== الخامس الابتدائي============
    wlb5 = Label(secwind, text=": الخامس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=190, y=310)

    wbtn21 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=xG0XkxhRZu4'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=200, y=350)

    wbtn22 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Ley_tTCTwpo&list=PLo81HqzE036q4Tifj_nXhzdYFIWlYZm5S'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=200, y=390)

    wbtn23 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=nx2-xp1UG4c'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=200, y=430)

    wbtn24 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=65oTDBzmqtI'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=200, y=470)

    wbtn25 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=t5zV7Ajm_v0'), text="        العلوم        ",
                    bg='#F0A500').place(x=200, y=510)

    wbtn35 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=psvAeYxt8cc'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=200, y=550)
# ===============================================

# ===السادس الابتدائي============================
    wlb6 = Label(secwind, text=": السادس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=29, y=310)

    wbtn26 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=CRUO0ddlk-Y'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=40, y=350)

    wbtn27 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=G-3rGLlJOr8'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=40, y=390)

    wbtn28 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=R3dFbe2CdKc'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=40, y=430)

    wbtn29 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=vwfMqzVVLPE'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=40, y=470)

    wbtn30 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=cGg2AnB_no0'), text="        العلوم        ",
                    bg='#F0A500').place(x=40, y=510)

    wbtn31 = Button(secwind, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=12JrIwc-KNA'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=40, y=550)

# =============================== دالة تحميل الكتب =============================================


def thrwin():
    thrwin = Tk()
    thrwin.geometry("480x600")
    thrwin.title("تحميل كتب المرحلة الابتدائية")
    thrwin.configure(background='#151D3B')
    thrwin.resizable(False, False)

    mlb = Label(thrwin, text=" تحميل الكتب الدراسية للمرحلة الابتدائية", bg='#151D3B',
                fg='white', font=("Tajawl", 14)).place(x=100, y=10)

# ====================== الاول الابتدائي===============================

    wlb1 = Label(thrwin,  text=": الاول الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=360, y=45)

    wbtn1 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1_Q0l-a3TVyYG1ggy70O19s6umHMA5h0y/view?usp=sharing'), text="التربية الاسلامية",
                   bg='#F0A500').place(x=360, y=75)

    wbtn2 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1HgBx7_0Y3CwnthrEyI3rlZz2bsMhrLZp/view?usp=sharing'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=360, y=115)

    wbtn3 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1NZkhlUY-_U6-DO_DMpxt28uiWljY-jMv/view?usp=sharing'), text="اللغة الانكليزية  ",
                   bg='#F0A500').place(x=360, y=155)

    wbtn4 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1fhxxBNoCxUi_gj0t4-gzsDO3h9SxSMt1/view?usp=sharing'), text="   الرياضيات     ",
                   bg='#F0A500').place(x=360, y=195)

    wbtn5 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1NxlZA83DUw57RgwpbJQkZE_Q3PgNzVu5/view?usp=sharing'), text="       العلوم        ",
                   bg='#F0A500').place(x=360, y=235)

# ==========================================================

# ================الثاني الابتدائي==========================

    wlb2 = Label(thrwin, text=": الثاني الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=200, y=45)

    wbtn6 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1W8_edy6ynr1ee6jk4buQLFzQ8_CTfN1N/view?usp=sharing'), text="التربية الاسلامية",
                   bg='#F0A500').place(x=200, y=75)

    wbtn7 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1XK7m2TwffuQuC2VebRCkHTL_MiLAbTiP/view?usp=sharing'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=200, y=115)

    wbtn8 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1ilrnp_zDnPL6Dq6x3_tSsrQhuiikImgj/view?usp=sharing'), text="  اللغة الانكليزية",
                   bg='#F0A500').place(x=200, y=155)

    wbtn9 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1zuNU47FFmCEOgaK4kfl93WUEsjzZwvfb/view?usp=sharing'), text="    الرياضيات    ",
                   bg='#F0A500').place(x=200, y=195)

    wbtn10 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1mvBOalgJbjXROmhi6kRQPkbqOU0Pv08b/view?usp=sharing'), text="        العلوم        ",
                    bg='#F0A500').place(x=200, y=235)
# ======================================================================

# ======================الثالث الابتدائي================================
    wlb3 = Label(thrwin, text=": الثالث الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=32, y=45)

    wbtn11 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/12uxDqQIIsdvMmH6kLThZ8TFm_vPas20n/view?usp=sharing'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=40, y=75)

    wbtn12 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/19r7cizG9NGyydmEVWvVPLR2EllgTv7Cz/view?usp=sharing'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=40, y=115)

    wbtn13 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1EGejLGTHrMt9NrwCwMMIQpBwuZqLBUOs/view?usp=sharing'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=40, y=155)

    wbtn14 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1bwMnMTQVhB-_SosCmmd845O04K3RJU3W/view?usp=sharing'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=40, y=195)

    wbtn15 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/17sewQhuOLP1Zbc4Sxi6vIMqlqm3GY3q6/view?usp=sharing'), text="        العلوم        ",
                    bg='#F0A500').place(x=40, y=235)
    # ==========================================================

    # =============الرابع الابتدائي=============================
    wlb4 = Label(thrwin, text=": الرابع الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=350, y=310)

    wbtn16 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1YidDMFcuBBcsK8RFo15JGFHhMrxhRDqB/view?usp=sharing'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=360, y=350)

    wbtn17 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1t--2H88AA8Fi-y4ZlISco6sd0zK2ss1l/view?usp=sharing'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=360, y=390)

    wbtn18 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/11HIB888QCKra8OwG8582K59xcLdXOhyV/view?usp=sharing'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=360, y=430)

    wbtn19 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1D75FfN2nbtaueommkxPqMUb6Y5X5YDJR/view?usp=sharing'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=360, y=470)

    wbtn20 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1JwWOgdulWb9ZRaMNXiI2dOMl8yS_8R2Z/view?usp=sharing'), text="        العلوم        ",
                    bg='#F0A500').place(x=360, y=510)

    wbtn39 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/14mQvYtomtWCoJIWllarUm-ZdB5MYQSAZ/view?usp=sharing'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=360, y=550)

# ========================================================================

    # =========================الخامس الابتدائي===========================

    wlb5 = Label(thrwin, text=": الخامس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=190, y=310)

    wbtn21 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1fGBq0lZ4yQnucPasuphkTWyEJI72pRkv/view'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=200, y=350)

    wbtn22 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1K4IkgHoFIcT13K_G5bKM6SpM3HlLJRRi/view?usp=sharing'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=200, y=390)

    wbtn23 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1FbRsq9cJ-H1N_YmWfsYmZAgh5NwPWmGd/view?usp=sharing'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=200, y=430)

    wbtn24 = Button(thrwin, command=lambda: webbrowser.open('https://up.mlazemna.com/bk5pmth/'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=200, y=470)

    wbtn25 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/15eQe92487aMZVCRNcyPKGNGHik2B7VgE/view?usp=sharing'), text="        العلوم        ",
                    bg='#F0A500').place(x=200, y=510)

    wbtn35 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1or9dw1q67XWCiQRlhCkbld0JWfntHd-U/view?usp=sharing'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=200, y=550)
# ===========================================================================

# ====================================السادس الابتدائي=======================

    wlb6 = Label(thrwin, text=": السادس الابتدائي", bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=32, y=310)

    wbtn26 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/14upGVPdPoRKN8iXC6Uf6bPrCHd3MiRNe/view?usp=drivesdk'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=40, y=350)

    wbtn27 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1N3WRxbiWMOjNJHnRIlRBUxP-Z062uKz6/view?usp=drivesdk'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=40, y=390)

    wbtn28 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1lEqZaU4RCx_2IGGltIGAaITTs9yADDR0/view?usp=drivesdk'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=40, y=430)

    wbtn29 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1PAgYLsuOjWEYj0U-k87enYk8_CX8L4CL/view?usp=drivesdk'), text="    الرياضيات    ",
                    bg='#F0A500').place(x=40, y=470)

    wbtn30 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1F2ZtcFwuau3J8E3fyFpBdiz_yTZ8H_Jw/view?usp=drivesdk'), text="        العلوم        ",
                    bg='#F0A500').place(x=40, y=510)

    wbtn31 = Button(thrwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1s1Dnv2VhVEyuotryBXBlI8qe45XuxWmt/view?usp=drivesdk'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=40, y=550)

# المرحلة المتوسطة ==============================================

# ======================دالة الدورس==================


def forwin():
    forwin = Tk()
    forwin.geometry('550x420')
    forwin.title("مشاهدة الدروس الالكترونية للمرحلة المتوسطة")

    forwin.configure(background='#151D3B')
    forwin.resizable(False, False)

    mlab = Label(forwin, text='مشاهدة الدروس الالكترونية للمرحلة المتوسطة ',  bg='#151D3B',
                 fg='white', font=("Tajawl", 14)).place(x=130, y=9)

    lab01 = Label(forwin, text='الاول المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=430, y=45)

    wbtn02 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Y6AneeTfPAY'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=430, y=85)

    wbtn03 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=H1FQAlHNLmw'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=430, y=125)

    wbtn04 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=kqh9bnIesbU'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=430, y=165)

    wbtn05 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=p9qeilISmyU'), text="    الرياضيات     ",
                    bg='#F0A500').place(x=430, y=205)

    wbtn06 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=IStqLTMN83M'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=430, y=245)

    wbtn07 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=2a_k7TR_gWk'), text="        العلوم        ",
                    bg='#F0A500').place(x=430, y=285)

    wbtn08 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Hl4t_g_MTqs'), text="     الحاسوب      ",
                    bg='#F0A500').place(x=430, y=325)

    # wbtn043 = Button(forwin, command=lambda: webbrowser.open(''), text="  نشاط انكليزي  ",
    #                  bg='#F0A500').place(x=430, y=365)

# ================= دول تحميل كتب المرحلة المتوسطة====================================


# =====================================الثاني المتوسط=========================

    frlabel = Label(forwin, text='الثاني المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=230, y=45)

    wbtn02 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=zX3wf1LXXwc'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=230, y=85)

    wbtn03 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=wvR60_wrlCI'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=230, y=125)

    wbtn04 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=pQscpKarXRk'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=230, y=165)

    wbtn05 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=n5dKEkj1a0U'), text="    الرياضيات     ",
                    bg='#F0A500').place(x=230, y=205)

    wbtn06 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=abCLewhBNr8'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=230, y=245)

    wbtn07 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=jFpYXTeJElc'), text="        العلوم        ",
                    bg='#F0A500').place(x=230, y=285)

    wbtn08 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=6bPwSNXt8Mw'), text="     الحاسوب      ",
                    bg='#F0A500').place(x=230, y=325)

    # wbtn032 = Button(forwin, command=lambda: webbrowser.open(''), text="  نشاط انكليزي  ",
    #                  bg='#F0A500').place(x=230, y=365)


# =======================الثالث المتوسط========================================

    lab01 = Label(forwin, text='الثالث المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=60, y=45)

    wbtn02 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=LNpcAKzFfGo'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=60, y=85)

    wbtn03 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=13VxJrFr-yA'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=60, y=125)

    wbtn04 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=d3t5VZRwnxk'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=60, y=165)

    wbtn05 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=4raGqrjjTpc'), text="    الرياضيات     ",
                    bg='#F0A500').place(x=60, y=205)

    wbtn06 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=8R0tq8WmtoI'), text="        الاحياء      ",
                    bg='#F0A500').place(x=60, y=245)

    wbtn07 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=bs-t4ij3ET4'), text="      الكيمياء       ",
                    bg='#F0A500').place(x=60, y=285)

    wbtn08 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=YmttZp5gQsE'), text="      الفيزياء       ",
                    bg='#F0A500').place(x=60, y=325)

    wbtn08 = Button(forwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=_TmNI3k5e44'), text="    الاجتماعيات   ",
                    bg='#F0A500').place(x=60, y=365)

    # wbtn08 = Button(forwin, command=lambda: webbrowser.open(''), text="  نشاط انكليزي  ",
    #                 bg='#F0A500').place(x=60, y=405)

# ========================== تحميل كتب المرحلة المتوسطة ================================================================


def fifwin():
    fifwin = Tk()
    fifwin.geometry('550x440')
    fifwin.title("تحميل الكتب المدرسية للمرحلة المتوسطة")

    fifwin.configure(background='#151D3B')
    fifwin.resizable(False, False)

    mlab = Label(fifwin, text='تحميل الكتب المدرسية للمرحلة المتوسطة',  bg='#151D3B',
                 fg='white', font=("Tajawl", 14)).place(x=130, y=9)

# ======================== الاول المتوسط ===================================================================================

    lab01 = Label(fifwin, text='الاول المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=430, y=45)

    wbtn02 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1XugelslkDLsJSyIOdVCF7tLFO9OU20kU/view?usp=drivesdk'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=430, y=85)

    wbtn03 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/13C6XYzlagggifuipjNXaXkrbAH42QaAa/view?usp=drivesdk'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=430, y=125)

    wbtn04 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1c1sH1cfDeFUNPlSTXvR5ADA0JUbZp1he/view?usp=drivesdk'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=430, y=165)

    wbtn05 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1BxuzYSeX6sgWV4EnXaWiCdF8neLFpPp9/view?usp=drivesdk'), text="    الرياضيات     ",
                    bg='#F0A500').place(x=430, y=205)

    wbtn06 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1KYGmJyzDxWBu_KDUHwrFaUigktZoTjL_/view?usp=drivesdk'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=430, y=245)

    wbtn07 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1wkUldkdtBzp_hP2zj32QpdO5ON-bGSiy/view?usp=drivesdk'), text="        العلوم        ",
                    bg='#F0A500').place(x=430, y=285)

    wbtn08 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1aVXZA46Spdl6vRwlevoKu-y0tPnVTy_S/view'), text="     الحاسوب      ",
                    bg='#F0A500').place(x=430, y=325)

    wbtn043 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/101ejCAjnbbkpTGpzHRyCs_NlXeAiAePq/view?usp=drivesdk'), text="  نشاط انكليزي  ",
                     bg='#F0A500').place(x=430, y=365)


# ============================= الثاني المتوسط =====================================================

    frlabel = Label(fifwin, text='الثاني المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=230, y=45)

    wbtn02 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/14pgtWeXppYTpceympnB8TEo9PGrgngos/view?usp=drivesdk'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=230, y=85)

    wbtn03 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Z7GG9D6NRChnAkrG_Og7WTwRZExlmioq/view?usp=drivesdk'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=230, y=125)

    wbtn04 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/16nt3SBFj2XhdDU_VwfkOssqTKCTRHh0n/view?usp=drivesdk'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=230, y=165)

    wbtn05 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1sdn2LnJlvtvy0mYSlrqKMyEgVxkef9a_/view?usp=drivesdk'), text="    الرياضيات     ",
                    bg='#F0A500').place(x=230, y=205)

    wbtn06 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1LTY_LXqQCMmAzybqQjwc-w5lL2hjNhSW/view?usp=drivesdk'), text="   الاجتماعيات   ",
                    bg='#F0A500').place(x=230, y=245)

    wbtn07 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1N6XWY7YWqjSVbI4ZHwIQumv239_4wQKp/view?usp=drivesdk'), text="        العلوم        ",
                    bg='#F0A500').place(x=230, y=285)

    wbtn08 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1PxsNq0apdzz5JQNWHTYRXrAOQ8o9nuFN/view?usp=drivesdk'), text="     الحاسوب      ",
                    bg='#F0A500').place(x=230, y=325)

    wbtn032 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1HrUrQKiuV4G2IZ2IyrQFnw52JuH-w2ll/view?usp=drivesdk'), text="  نشاط انكليزي  ",
                     bg='#F0A500').place(x=230, y=365)

# =============================== الثالث المتوسط ============================================

    lab01 = Label(fifwin, text='الثالث المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=60, y=45)

    wbtn02 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1qwOHgZ3PxaNS9KO5ZAZMYnWJJTCeA4V8/view?usp=drivesdk'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=60, y=85)

    wbtn03 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1NvaW05t8LGm9CB8v6kvWXGYEbRsTh01D/view?usp=drivesdk'), text="   اللغة العربية   ",
                    bg='#F0A500').place(x=60, y=125)

    wbtn04 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1LT-z3zTHUnKRyBfStkqN5Ufqnv_IZdUz/view?usp=drivesdk'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=60, y=165)

    wbtn05 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1I7-d_rm-XBGfBameYaGVnZopvRWSRTFn/view?usp=drivesdk'), text="    الرياضيات     ",
                    bg='#F0A500').place(x=60, y=205)

    wbtn06 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1tViA_Pvn5APxOU9NOttrjanIx56ha95m/view?usp=drivesdk'), text="        الاحياء      ",
                    bg='#F0A500').place(x=60, y=245)

    wbtn07 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Eu8_oJTCvASDsvf9IoYU0JKQPJe6v2iu/view?usp=drivesdk'), text="      الكيمياء       ",
                    bg='#F0A500').place(x=60, y=285)

    wbtn08 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Yny7veebNVjgWNSJhsoEaRhpQvIz_9fC/view?usp=drivesdk'), text="      الفيزياء       ",
                    bg='#F0A500').place(x=60, y=325)

    wbtn08 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1pXNqxN2RCNmnpxhRTgGnOx-gNsIpBT7C/view'), text="    الاجتماعيات   ",
                    bg='#F0A500').place(x=60, y=365)

    wbtn08 = Button(fifwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/179ZWDse8jFHHYQ1qGgymzeRDOIas2dDZ/view?usp=drivesdk'), text="  نشاط انكليزي  ",
                    bg='#F0A500').place(x=60, y=405)


# ---------------------------- المرحلة الاعدادية ------------------------------------------------------


# def sevein():
#     sevein = Tk()
#     sevein.geometry()
#     sevein.geometry('500x450')
#     sevein.configure(background='#151D3B')

#     slab = Label(sevein, text='الخامس الاحيائي', bg='#151D3B',  fg='white', font=(
#         "Tajawl", 13, 'bold')).place(x=370, y=45)

#     sbtn02 = Button(sevein, command=lambda: webbrowser.open(''), text="التربية الاسلامية",
#                     bg='#F0A500').place(x=370, y=85)

#     sbtn03 = Button(sevein, command=lambda: webbrowser.open(''), text="   اللغة العربية   ",
#                     bg='#F0A500').place(x=370, y=125)

#     sbtn04 = Button(sevein, command=lambda: webbrowser.open(''), text="  اللغة الانكليزية",
#                     bg='#F0A500').place(x=370, y=165)

#     sbtn05 = Button(sevein, command=lambda: webbrowser.open(''), text="    الرياضيات     ",
#                     bg='#F0A500').place(x=370, y=205)

#     sbtn06 = Button(sevein, command=lambda: webbrowser.open(''), text="        الاحياء      ",
#                     bg='#F0A500').place(x=370, y=245)

#     sbtn07 = Button(sevein, command=lambda: webbrowser.open(''), text="      الكيمياء       ",
#                     bg='#F0A500').place(x=370, y=285)

#     sbtn08 = Button(sevein, command=lambda: webbrowser.open(''), text="      الفيزياء       ",
#                     bg='#F0A500').place(x=370, y=325)
#     sbtn033 = Button(sevein, command=lambda: webbrowser.open(''), text="     الحاسوب      ",
#                      bg='#F0A500').place(x=370, y=365)

#     sbtn09 = Button(sevein, command=lambda: webbrowser.open(''), text="  نشاط انكليزي ",
#                     bg='#F0A500').place(x=370, y=405)


#  ---------------------------- شاشه اختيار الفرع ----------------------------------------------
def sixwin():
    sixwin = Tk()
    sixwin.geometry('450x270')
    sixwin.title("اختر فرعك الدراسي")
    sixwin.configure(background='#151D3B')
    sixwin.resizable(False, False)

    mlabs = Label(sixwin, text='اختر فرعك الدراسي', fg='#F0A500',  bg='#151D3B',
                  font=("Tajawl", 19, 'bold')).place(x=140, y=25)

# ------------------------------------------------------------------------------

    malb = Label(sixwin, text='الرابع الاعدادي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 15, 'bold')).place(x=320, y=90)

    fsbtn = Button(sixwin, command=eiwin, text='   علمي   ',
                   bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=335, y=140)

    fsbtn = Button(sixwin, command=niwin, text='   ادبي    ',
                   bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=335, y=190)

# -----------------------------------------------------------------------------------------

    mal2 = Label(sixwin, text='الخامس الاعدادي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 15, 'bold')).place(x=170, y=90)

    fsbtn = Button(sixwin, command=tewin,  text='   احيائي   ',
                   bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=190, y=140)

    fsbtn2 = Button(sixwin, command=elwin, text='   تطبيقي  ',
                    bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=190, y=180)

    fsbtn3 = Button(sixwin, command=tuwin,  text='    ادبي    ',
                    bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=190, y=220)


# ----------------------------------------------------------------------------------------
    mal2 = Label(sixwin, text='السادس الاعدادي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 15, 'bold')).place(x=25, y=90)

    fsbtn = Button(sixwin, command=thwin, text='   احيائي   ',
                   bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=45, y=140)

    fsbtn2 = Button(sixwin, command=ftwin, text='   تطبيقي  ',
                    bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=45, y=180)

    fsbtn3 = Button(sixwin, command=fthwin, text='    ادبي    ',
                    bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=45, y=220)
# -------------------------------------------------------------------------------------------------------


# ---------------------- دروس الرابع اعدادي ------------------------------------
def eiwin():  # العلمي
    eiwin = Tk()
    eiwin.geometry('200x440')
    eiwin.title("دروس الرابع العلمي")
    eiwin.configure(background='#151D3B')
    eiwin.resizable(False, False)

    mlab = Label(eiwin, text='دروس الرابع العلمي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b1 = Button(eiwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=2VI4dNaQspQ'), text="التربية الاسلامية",
                bg='#F0A500').place(x=60, y=85)

    b2 = Button(eiwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=wAO14zSz4HQ'), text="   اللغة العربية   ",
                bg='#F0A500').place(x=60, y=125)

    b3 = Button(eiwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=vIua-THo4-k'), text="  اللغة الانكليزية",
                bg='#F0A500').place(x=60, y=165)

    b4 = Button(eiwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=zhk1YbyE0cM'), text="    الرياضيات     ",
                bg='#F0A500').place(x=60, y=205)

    b5 = Button(eiwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=JzGOu9TNOLk'), text="        الاحياء      ",
                bg='#F0A500').place(x=60, y=245)

    b6 = Button(eiwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=fTqaF_WBprQ'), text="      الكيمياء       ",
                bg='#F0A500').place(x=60, y=285)

    b7 = Button(eiwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Yx4PSiqVhX4'), text="      الفيزياء       ",
                bg='#F0A500').place(x=60, y=325)

    b9 = Button(eiwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=zhPKQrxzO4s'), text="      الحاسوب     ",
                bg='#F0A500').place(x=60, y=365)

# -------------------------------------------------------------


def niwin():  # الادبي
    niwin = Tk()
    niwin.geometry('200x440')
    niwin.title("دروس الرابع الادبي")
    niwin.configure(background='#151D3B')
    niwin.resizable(False, False)

    mlab1 = Label(niwin, text='دروس الرابع الادبي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b10 = Button(niwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=2VI4dNaQspQ'), text="التربية الاسلامية",
                 bg='#F0A500').place(x=60, y=85)

    b20 = Button(niwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=wAO14zSz4HQ'), text="   اللغة العربية   ",
                 bg='#F0A500').place(x=60, y=125)

    b30 = Button(niwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=vIua-THo4-k'), text="  اللغة الانكليزية",
                 bg='#F0A500').place(x=60, y=165)

    b40 = Button(niwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=YaVozOuRHgw'), text="    الرياضيات     ",
                 bg='#F0A500').place(x=60, y=205)

    b50 = Button(niwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=o6A8iYMqmeE'), text="        التاريخ      ",
                 bg='#F0A500').place(x=60, y=245)

    b60 = Button(niwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Q4hxN92xqZU'), text="     الجغرافيه      ",
                 bg='#F0A500').place(x=60, y=285)

    b70 = Button(niwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=uliKWWY9BtM'), text="  علم الاجتماع    ",
                 bg='#F0A500').place(x=60, y=325)

    b80 = Button(niwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=zhPKQrxzO4s'), text="      الحاسوب     ",
                 bg='#F0A500').place(x=60, y=365)

# -------------------------------------------------------------------------------------------------

# ----------------------------- دروس الخامس الاعدادي ---------------------------------------------


def tewin():  # الاحيائي
    tewin = Tk()
    tewin.title("دروس الخامس الاحيائي")
    tewin.geometry('200x440')
    tewin.configure(background='#151D3B')
    tewin.resizable(False, False)

    mlab10 = Label(tewin, text='دروس الخامس الاحيائي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b100 = Button(tewin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=hntoM-0Zr3Q'), text="التربية الاسلامية",
                  bg='#F0A500').place(x=60, y=85)

    b200 = Button(tewin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=xXswT_1q8cM'), text="   اللغة العربية   ",
                  bg='#F0A500').place(x=60, y=125)

    b300 = Button(tewin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=-OeLa4Z0BoI'), text="  اللغة الانكليزية",
                  bg='#F0A500').place(x=60, y=165)

    b400 = Button(tewin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=-rN6GyYmhD8'), text="    الرياضيات     ",
                  bg='#F0A500').place(x=60, y=205)

    b500 = Button(tewin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=oBrLQHmyP2E'), text="        الاحياء      ",
                  bg='#F0A500').place(x=60, y=245)

    b600 = Button(tewin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=G_Lmb5WWDhk'), text="      الكيمياء       ",
                  bg='#F0A500').place(x=60, y=285)

    b700 = Button(tewin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=5EP7EaESMR8'), text="      الفيزياء       ",
                  bg='#F0A500').place(x=60, y=325)

    b800 = Button(tewin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=jATa4h8hGR8'), text="      الحاسوب     ",
                  bg='#F0A500').place(x=60, y=365)
# --------------------------------------------------------------------------------------------------------------


def elwin():  # التطبيقي
    elwin = Tk()
    elwin.geometry('200x440')
    elwin.title("دروس الخامس التطبيقي")
    elwin.configure(background='#151D3B')
    elwin.resizable(False, False)

    mlab10 = Label(elwin, text='دروس الخامس التطبيقي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b100 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=hntoM-0Zr3Q'), text="التربية الاسلامية",
                  bg='#F0A500').place(x=60, y=85)

    b200 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=xXswT_1q8cM'), text="   اللغة العربية   ",
                  bg='#F0A500').place(x=60, y=125)

    b300 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=-OeLa4Z0BoI'), text="  اللغة الانكليزية",
                  bg='#F0A500').place(x=60, y=165)

    b400 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=-rN6GyYmhD8'), text="    الرياضيات     ",
                  bg='#F0A500').place(x=60, y=205)

    b400 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=XT4Uf-3lSw4'), text="       اقتصاد        ",
                  bg='#F0A500').place(x=60, y=245)

    b400 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Mra7PmbMwrM'), text="    علم الارض     ",
                  bg='#F0A500').place(x=60, y=285)

    b600 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=G_Lmb5WWDhk'), text="      الكيمياء       ",
                  bg='#F0A500').place(x=60, y=325)

    b700 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=5EP7EaESMR8'), text="      الفيزياء       ",
                  bg='#F0A500').place(x=60, y=365)

    b8030 = Button(elwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=jATa4h8hGR8'), text="      الحاسوب     ",
                   bg='#F0A500').place(x=60, y=405)
# -----------------------------------------------------------------


def tuwin():  # الادبي
    tuwin = Tk()
    tuwin.geometry('200x400')
    tuwin.title("دروس الخامس الادبي")
    tuwin.configure(background='#151D3B')
    tuwin.resizable(False, False)

    mlab109 = Label(tuwin, text='دروس الخامس الادبي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b1008 = Button(tuwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=hntoM-0Zr3Q'), text="التربية الاسلامية",
                   bg='#F0A500').place(x=60, y=85)

    b2007 = Button(tuwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=xXswT_1q8cM'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=60, y=125)

    b3006 = Button(tuwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=-OeLa4Z0BoI'), text="  اللغة الانكليزية",
                   bg='#F0A500').place(x=60, y=165)

    b4005 = Button(tuwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=3-S76mDiQWY'), text="    الرياضيات     ",
                   bg='#F0A500').place(x=60, y=205)

    b5004 = Button(tuwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=SEu2EFVKtN0'), text="      التاريخ        ",
                   bg='#F0A500').place(x=60, y=245)

    b6003 = Button(tuwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=qHtMy31krOk'), text="     الجغرافية      ",
                   bg='#F0A500').place(x=60, y=285)

    b7002 = Button(tuwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=m1KJuqtksEk'), text="      الفلسفة       ",
                   bg='#F0A500').place(x=60, y=325)

    b8200 = Button(tuwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=jATa4h8hGR8'), text="      الحاسوب     ",
                   bg='#F0A500').place(x=60, y=365)

# --------------------------------------------------------------------------------------------------------

# =================================== السادس الاعدادي ==========+++++++++++++++++++++++++=================


def thwin():  # الاحيائي

    thwin = Tk()
    thwin.geometry('200x440')
    thwin.title("دروس السادس الاحيائي ")
    thwin.configure(background='#151D3B')
    thwin.resizable(False, False)

    mlab1092 = Label(thwin, text='دروس السادس الاحيائي ', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b10082 = Button(thwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=FYbM8USDUwk'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=60, y=85)

    b20072 = Button(thwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=6Bgn_1IjXMY'), text="       القواعد       ",
                    bg='#F0A500').place(x=60, y=125)

    b20072 = Button(thwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=uE2Rn0JlO_o'), text="        الادب        ",
                    bg='#F0A500').place(x=60, y=165)

    b30062 = Button(thwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=3RgsOm45sj0'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=60, y=205)

    b40052 = Button(thwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=SC3fwX6MPCs'), text="    الرياضيات     ",
                    bg='#F0A500').place(x=60, y=245)

    b50042 = Button(thwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=7pMtGEhGz1s'), text="        الاحياء      ",
                    bg='#F0A500').place(x=60, y=285)

    b60032 = Button(thwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=O9sUfJXhwZU'), text="      الكيمياء       ",
                    bg='#F0A500').place(x=60, y=325)

    b70022 = Button(thwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=NarJJURWYd4'), text="      الفيزياء       ",
                    bg='#F0A500').place(x=60, y=365)
    # ---------------------------------------------------------------------------


def ftwin():  # التطبيقي

    ftwin = Tk()
    ftwin.geometry('200x440')
    ftwin.title("دروس السادس التطبيقي ")
    ftwin.configure(background='#151D3B')
    ftwin.resizable(False, False)

    mlab10932 = Label(ftwin, text='دروس السادس التطبيقي ', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b100832 = Button(ftwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=FYbM8USDUwk'), text="التربية الاسلامية",
                     bg='#F0A500').place(x=60, y=85)

    b200732 = Button(ftwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=6Bgn_1IjXMY'), text="       القواعد       ",
                     bg='#F0A500').place(x=60, y=125)

    b200732 = Button(ftwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=uE2Rn0JlO_o'), text="        الادب        ",
                     bg='#F0A500').place(x=60, y=165)

    b300362 = Button(ftwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=3RgsOm45sj0'), text="  اللغة الانكليزية",
                     bg='#F0A500').place(x=60, y=205)

    b400352 = Button(ftwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=SC3fwX6MPCs'), text="    الرياضيات     ",
                     bg='#F0A500').place(x=60, y=245)

    b500342 = Button(ftwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=xEg_QsohOtQ'), text="       الاقتصاد     ",
                     bg='#F0A500').place(x=60, y=285)

    b600332 = Button(ftwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=O9sUfJXhwZU'), text="      الكيمياء       ",
                     bg='#F0A500').place(x=60, y=325)

    b700232 = Button(ftwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=fcgOm0MSpo0'), text="      الفيزياء       ",
                     bg='#F0A500').place(x=60, y=365)
# -------------------------------------------------------------------------------------------------------


def fthwin():  # الادبي

    fthwin = Tk()
    fthwin.geometry('200x440')
    fthwin.title("دروس السادس الادبي ")
    fthwin.configure(background='#151D3B')
    fthwin.resizable(False, False)

    mlab109432 = Label(fthwin, text='دروس السادس الادبي ', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b1008342 = Button(fthwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=FYbM8USDUwk'), text="التربية الاسلامية",
                      bg='#F0A500').place(x=60, y=85)

    b2007432 = Button(fthwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=6Bgn_1IjXMY'), text="       القواعد       ",
                      bg='#F0A500').place(x=60, y=125)

    b2007432 = Button(fthwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=uE2Rn0JlO_o'), text="        الادب        ",
                      bg='#F0A500').place(x=60, y=165)

    b3003462 = Button(fthwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=3RgsOm45sj0'), text="  اللغة الانكليزية",
                      bg='#F0A500').place(x=60, y=205)

    b4003452 = Button(fthwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=paC1gxXG3lI'), text="    الرياضيات     ",
                      bg='#F0A500').place(x=60, y=245)

    b5003442 = Button(fthwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=ey9Kl2Einzk'), text="      الاقتصاد      ",
                      bg='#F0A500').place(x=60, y=285)

    b6003342 = Button(fthwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=sjOJv3jZzfg'), text="      التاريخ        ",
                      bg='#F0A500').place(x=60, y=325)

    b7002324 = Button(fthwin, command=lambda: webbrowser.open('https://www.youtube.com/watch?v=2xpctNSD1hk'), text="     الجغرافيه      ",
                      bg='#F0A500').place(x=60, y=365)
# ------------------------------------------------------------


# -------------- كتب المرحلة الاعدادية --------------------------------------------

# الرابع العلمي
def sithwin():
    sithwin = Tk()
    sithwin.geometry('450x270')
    sithwin.title("اختر فرعك الدراسي ")
    sithwin.configure(background='#151D3B')
    sithwin.resizable(False, False)
    mlabs = Label(sithwin, text='اختر فرعك الدراسي', fg='#F0A500',  bg='#151D3B',
                  font=("Tajawl", 19, 'bold')).place(x=140, y=25)

# ------------------------------------------------------------------------------

    malb = Label(sithwin, text='الرابع الاعدادي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 15, 'bold')).place(x=320, y=90)

    fsbtn = Button(sithwin, command=sethwin, text='   علمي   ',
                   bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=335, y=140)

    fsbtn = Button(sithwin, command=nithwin, text='   ادبي    ',
                   bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=335, y=190)

# -----------------------------------------------------------------------------------------

    mal2 = Label(sithwin, text='الخامس الاعدادي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 15, 'bold')).place(x=170, y=90)

    fsbtn = Button(sithwin, command=twwin,  text='   احيائي   ',
                   bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=190, y=140)

    fsbtn2 = Button(sithwin, command=tonwin, text='   تطبيقي  ',
                    bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=190, y=180)

    fsbtn3 = Button(sithwin, command=ttwwin, text='    ادبي    ',
                    bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=190, y=220)


# ----------------------------------------------------------------------------------------
    mal2 = Label(sithwin, text='السادس الاعدادي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 15, 'bold')).place(x=25, y=90)

    fsbtn = Button(sithwin, command=twthwin, text='   احيائي   ',
                   bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=45, y=140)

    fsbtn2 = Button(sithwin, command=twfowin, text='   تطبيقي  ',
                    bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=45, y=180)

    fsbtn3 = Button(sithwin, command=twfiwin, text='    ادبي    ',
                    bg='#F0A500', fg='black', font=("Tajawl", 13, 'bold')).place(x=45, y=220)

# ----------------------------------------------------------------------------------------


def sethwin():  # العلمي
    sethwin = Tk()
    sethwin.geometry('200x440')
    sethwin.title("كتب الرابع العلمي")
    sethwin.configure(background='#151D3B')
    sethwin.resizable(False, False)
    mlab = Label(sethwin, text='كتب الرابع العلمي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b1 = Button(sethwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1b-WEUZcDu3zNBjhlPkPF8hRToRzkOS0M/view'), text="التربية الاسلامية",
                bg='#F0A500').place(x=60, y=85)

    b2 = Button(sethwin, command=lambda: webbrowser.open('http://manahj.edu.iq/upload/upfile/ar/1155.pdf'), text="   اللغة العربية   ",
                bg='#F0A500').place(x=60, y=125)

    b3 = Button(sethwin, command=lambda: webbrowser.open('https://drive.google.com/u/0/uc?id=1C3gjwWuQ_7kSbJQ7vQzQV44WZNWmAYXJ&export=download'), text="  اللغة الانكليزية",
                bg='#F0A500').place(x=60, y=165)

    b4 = Button(sethwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1RJ8eUhBsl5ggY-f3wcbnobhwyoZvFTJ_/view'), text="    الرياضيات     ",
                bg='#F0A500').place(x=60, y=205)

    b5 = Button(sethwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1E9fn5Gi_xTbyqNBaNhYMKmB7Eg1p_wjk/view'), text="        الاحياء      ",
                bg='#F0A500').place(x=60, y=245)

    b6 = Button(sethwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1055DilEfBReuNgy2dlQ_sqFyRK4EmqDh/view'), text="      الكيمياء       ",
                bg='#F0A500').place(x=60, y=285)

    b7 = Button(sethwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1JCj4BMiz8Jj5DK-4Asq5NrYR_afA23hu/view'), text="      الفيزياء       ",
                bg='#F0A500').place(x=60, y=325)

    b9 = Button(sethwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Qq0ZPFpF-uD1cST7e1JnXjdpYsKMdnzg/view'), text="      الحاسوب     ",
                bg='#F0A500').place(x=60, y=365)

# ========================================================================================


def nithwin():  # الادبي
    nithwin = Tk()
    nithwin.geometry('200x440')
    nithwin.title("كتب الرابع الادبي")
    nithwin.configure(background='#151D3B')
    nithwin.resizable(False, False)

    mlab1 = Label(nithwin, text='كتب الرابع الادبي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b10 = Button(nithwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1ZcxXas2FgLy_yVIcLUuIkzf9GU3X4VPB/view?usp=drivesdk'), text="التربية الاسلامية",
                 bg='#F0A500').place(x=60, y=85)

    b20 = Button(nithwin, command=lambda: webbrowser.open('http://manahj.edu.iq/upload/upfile/ar/1155.pdf'), text="   اللغة العربية   ",
                 bg='#F0A500').place(x=60, y=125)

    b30 = Button(nithwin, command=lambda: webbrowser.open('https://drive.google.com/u/0/uc?id=1C3gjwWuQ_7kSbJQ7vQzQV44WZNWmAYXJ&export=download'), text="  اللغة الانكليزية",
                 bg='#F0A500').place(x=60, y=165)

    b40 = Button(nithwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1-Jc_XI_O9EpGukuCW_uYpQVkAZj8K72F/view?usp=drivesdk'), text="    الرياضيات     ",
                 bg='#F0A500').place(x=60, y=205)

    b50 = Button(nithwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1ZPVRZRxnJHR5yfJrifrJ-Q8SVRCPFvfy/view?usp=drivesdk'), text="        التاريخ      ",
                 bg='#F0A500').place(x=60, y=245)

    b60 = Button(nithwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1tQULmeUsyXXDSLq6ICIEov_L-_zJEFjA/view?usp=drivesdk'), text="    الجغرافيه       ",
                 bg='#F0A500').place(x=60, y=285)

    b70 = Button(nithwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1p0O48K1R7eXjLfhUDGpF0pEcrW5cCevP/view?usp=drivesdk'), text="  علم الاجتماع    ",
                 bg='#F0A500').place(x=60, y=325)

    b80 = Button(nithwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Qq0ZPFpF-uD1cST7e1JnXjdpYsKMdnzg/view'), text="      الحاسوب     ",
                 bg='#F0A500').place(x=60, y=365)

# =============================================================================================


def twwin():  # الاحيائي
    twwin = Tk()
    twwin.geometry('200x440')
    twwin.title("كتب الخامس الاحيائي")
    twwin.configure(background='#151D3B')
    twwin.resizable(False, False)

    mlab10 = Label(twwin, text='كتب الخامس الاحيائي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b100 = Button(twwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Atz-1jdYt9NZVy2B_TuuCvaUrOXC5vJv/view'), text="التربية الاسلامية",
                  bg='#F0A500').place(x=60, y=85)

    b200 = Button(twwin, command=lambda: webbrowser.open('https://www.amsebehm2017.com/2021/10/2022-pdf_19.html'), text="   اللغة العربية   ",
                  bg='#F0A500').place(x=60, y=125)

    b300 = Button(twwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1m-zzBTNrg2rNuCrxUdQD_azatPqvqrBw/view'), text="  اللغة الانكليزية",
                  bg='#F0A500').place(x=60, y=165)

    b400 = Button(twwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Beh0R-FXTNZjLygjjonQoyfq_ApuTXZD/view'), text="    الرياضيات     ",
                  bg='#F0A500').place(x=60, y=205)

    b500 = Button(twwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1bZZbuUn6Dw7zTVGjDx3pPv7pAiEa4mVL/view'), text="        الاحياء      ",
                  bg='#F0A500').place(x=60, y=245)

    b600 = Button(twwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/18y6bdYYD1ucBPXJSifHoL4owb5h-7wsO/view'), text="      الكيمياء       ",
                  bg='#F0A500').place(x=60, y=285)

    b700 = Button(twwin, command=lambda: webbrowser.open('https://drive.google.com/u/1/uc?id=1Q7ePIjt_eYyjHjWeqx2X7OG5kTtS5Boo&export=download'), text="      الفيزياء       ",
                  bg='#F0A500').place(x=60, y=325)

    b8000 = Button(twwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1wJbL27LVTz7ETLtcZ32I1g-F-f18uCFw/view'), text="  نشاط انكليزي ",
                   bg='#F0A500').place(x=60, y=365)

    b800 = Button(twwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1BT3GQ0ZYydJVg-ZENk4yI-U-Fl_nXmJz/view'), text="      الحاسوب     ",
                  bg='#F0A500').place(x=60, y=405)

# =================================================================================


def tonwin():  # التطبيقي
    tonwin = Tk()
    tonwin.geometry('200x480')
    tonwin.title("كتب الخامس التطبيقي")
    tonwin.configure(background='#151D3B')
    tonwin.resizable(False, False)
    mlab10 = Label(tonwin, text='كتب الخامس التطبيقي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b100 = Button(tonwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Atz-1jdYt9NZVy2B_TuuCvaUrOXC5vJv/view'), text="التربية الاسلامية",
                  bg='#F0A500').place(x=60, y=85)

    b200 = Button(tonwin, command=lambda: webbrowser.open('https://www.amsebehm2017.com/2021/10/2022-pdf_19.html'), text="   اللغة العربية   ",
                  bg='#F0A500').place(x=60, y=125)

    b300 = Button(tonwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1m-zzBTNrg2rNuCrxUdQD_azatPqvqrBw/view'), text="  اللغة الانكليزية",
                  bg='#F0A500').place(x=60, y=165)

    b400 = Button(tonwin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-math-5tatbiq.html'), text="    الرياضيات     ",
                  bg='#F0A500').place(x=60, y=205)

    b500 = Button(tonwin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-earth-science-5tatbiq.html'), text="      علم الارض   ",
                  bg='#F0A500').place(x=60, y=245)

    b600 = Button(tonwin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-chemistry-5tatbiq.html'), text="      الكيمياء       ",
                  bg='#F0A500').place(x=60, y=285)

    b700 = Button(tonwin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-physics-5tatbiq.html'), text="      الفيزياء       ",
                  bg='#F0A500').place(x=60, y=325)

    b800 = Button(tonwin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-activity-english-5tatbiq.html'), text="        اقتصاد       ",
                  bg='#F0A500').place(x=60, y=365)

    b800 = Button(tonwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1BT3GQ0ZYydJVg-ZENk4yI-U-Fl_nXmJz/view'), text="      الحاسوب      ",
                  bg='#F0A500').place(x=60, y=405)

    b800 = Button(tonwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1wJbL27LVTz7ETLtcZ32I1g-F-f18uCFw/view'), text="  نشاط انكليزي  ",
                  bg='#F0A500').place(x=60, y=445)


# ===============================================================================


def ttwwin():  # الادبي
    ttwwin = Tk()
    ttwwin.geometry('200x480')
    ttwwin.title("كتب الخامس الادبي")
    ttwwin.configure(background='#151D3B')
    ttwwin.resizable(False, False)

    mlab109 = Label(ttwwin, text='كتب الخامس الادبي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b1008 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1JAcjQiRZChOkFIJDOIL1e2uBWv7CdJbq/view'), text="التربية الاسلامية",
                   bg='#F0A500').place(x=60, y=85)

    b2007 = Button(ttwwin, command=lambda: webbrowser.open('https://www.amsebehm2017.com/2021/10/2022-pdf_19.html'), text="   اللغة العربية   ",
                   bg='#F0A500').place(x=60, y=125)

    b3006 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1mUYwBLE12jjD6aTArdF6vJGRFxKMBJxH/view'), text="  اللغة الانكليزية",
                   bg='#F0A500').place(x=60, y=165)

    b4005 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1D7kopU6-dNSj4Q_WvLjwKARSrWBtvLsX/view'), text="    الرياضيات     ",
                   bg='#F0A500').place(x=60, y=205)

    b5004 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1u0kWlX44RxnNjMzk5Ome71tYxs-OcPtS/view'), text="        البلاغة      ",
                   bg='#F0A500').place(x=60, y=245)

    b6003 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/13exLvAl8W6LBIKb_7ts8brTaIySt0f-_/view'), text="      التاريخ        ",
                   bg='#F0A500').place(x=60, y=285)

    b7002 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/14PJf2hV1Xviu6Vl2ELiA6yDUOWn-nx3R/view'), text="     الجغرافية      ",
                   bg='#F0A500').place(x=60, y=325)

    b8001 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1BT3GQ0ZYydJVg-ZENk4yI-U-Fl_nXmJz/view'), text="      الحاسوب     ",
                   bg='#F0A500').place(x=60, y=365)

    b8001 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1YH8MSCA4G-B02tqz74itvEZF2t1qUmds/view'), text="     علم النفس     ",
                   bg='#F0A500').place(x=60, y=405)

    b8001 = Button(ttwwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1wJbL27LVTz7ETLtcZ32I1g-F-f18uCFw/view'),  text="  نشاط انكليزي  ",
                   bg='#F0A500').place(x=60, y=445)


# =================================== السادس الاعدادي ==========+++++++++++++++++++++++++=================


def twthwin():  # الاحيائي

    twthwin = Tk()
    twthwin.geometry('200x440')
    twthwin.title("كتب السادس الاحيائي ")
    twthwin.configure(background='#151D3B')
    twthwin.resizable(False, False)

    mlab1092 = Label(twthwin, text='كتب السادس الاحيائي ', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b10082 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1aezDRFxXZBL_R7hLyGymgiwRogXSfeL6/view'), text="التربية الاسلامية",
                    bg='#F0A500').place(x=60, y=85)

    b20072 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1W_87PmC4hDEydw2HmRjwn8rwZHt94Fwz/view'), text="       القواعد       ",
                    bg='#F0A500').place(x=60, y=125)

    b20072 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Jz1FDbPe8Q3K6EbbCDXvgnffTshkisXp/view'), text="        الادب        ",
                    bg='#F0A500').place(x=60, y=165)

    b30062 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1LtlYRfsCG3HcEiEklffD7mwuis6WvGXd/view'), text="  اللغة الانكليزية",
                    bg='#F0A500').place(x=60, y=205)

    b40052 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1mTLGzTqHBE_QRQdHFFZwv7ooeneS-Uq7/view'), text="    الرياضيات     ",
                    bg='#F0A500').place(x=60, y=245)

    b50042 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1wl-Jl6rjfw7SL-r2pkvrhJ_T30zc-f5p/view'), text="        الاحياء      ",
                    bg='#F0A500').place(x=60, y=285)

    b60032 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1ORF58z8oLtDyPYoa3imDZeCQWPRVvdgF/view'), text="      الكيمياء       ",
                    bg='#F0A500').place(x=60, y=325)

    b70022 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/17n7XjwiVCNHzC4fYQvDWJG9QEEGtQeqd/view'), text="      الفيزياء       ",
                    bg='#F0A500').place(x=60, y=365)

    b70022 = Button(twthwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1EIGdg7Io6AOs1zEgOoWJDq_a_cDkc7pl/view'), text="  نشاط انكليزي  ",
                    bg='#F0A500').place(x=60, y=405)

    # ---------------------------------------------------------------------------


def twfowin():  # التطبيقي

    twfowin = Tk()
    twfowin.geometry('200x440')
    twfowin.title("كتب السادس التطبيقي ")
    twfowin.configure(background='#151D3B')
    twfowin.resizable(False, False)

    mlab10932 = Label(twfowin, text='كتب السادس التطبيقي ', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b100832 = Button(twfowin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1aezDRFxXZBL_R7hLyGymgiwRogXSfeL6/view'), text="التربية الاسلامية",
                     bg='#F0A500').place(x=60, y=85)

    b200732 = Button(twfowin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1W_87PmC4hDEydw2HmRjwn8rwZHt94Fwz/view'), text="       القواعد       ",
                     bg='#F0A500').place(x=60, y=125)

    b200732 = Button(twfowin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Jz1FDbPe8Q3K6EbbCDXvgnffTshkisXp/view'), text="        الادب        ",
                     bg='#F0A500').place(x=60, y=165)

    b300362 = Button(twfowin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1LtlYRfsCG3HcEiEklffD7mwuis6WvGXd/view'), text="  اللغة الانكليزية",
                     bg='#F0A500').place(x=60, y=205)

    b400352 = Button(twfowin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-math-6tatbiq.html'), text="    الرياضيات     ",
                     bg='#F0A500').place(x=60, y=245)

    b500342 = Button(twfowin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-aqtsad-6tatbiq.html'), text="       الاقتصاد     ",
                     bg='#F0A500').place(x=60, y=285)

    b600332 = Button(twfowin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-chemistry-6tatbiq.html'), text="      الكيمياء       ",
                     bg='#F0A500').place(x=60, y=325)

    b700232 = Button(twfowin, command=lambda: webbrowser.open('https://www.stadiraq.com/2020/10/book-physics-6tatbiq.html'), text="      الفيزياء       ",
                     bg='#F0A500').place(x=60, y=365)

    b700232 = Button(twfowin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1EIGdg7Io6AOs1zEgOoWJDq_a_cDkc7pl/view'), text="  نشاط انكليزي  ",
                     bg='#F0A500').place(x=60, y=405)
# -------------------------------------------------------------------------------------------------------


def twfiwin():  # الادبي

    twfiwin = Tk()
    twfiwin.geometry('200x440')
    twfiwin.title("كتب السادس الادبي ")
    twfiwin.configure(background='#151D3B')
    twfiwin.resizable(False, False)

    mlab109432 = Label(twfiwin, text='كتب السادس الادبي ', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=30)

    b1008342 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1aezDRFxXZBL_R7hLyGymgiwRogXSfeL6/view'), text="التربية الاسلامية",
                      bg='#F0A500').place(x=60, y=85)

    b2007432 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1W_87PmC4hDEydw2HmRjwn8rwZHt94Fwz/view'), text="       القواعد       ",
                      bg='#F0A500').place(x=60, y=125)

    b2007432 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1Jz1FDbPe8Q3K6EbbCDXvgnffTshkisXp/view'), text="        الادب        ",
                      bg='#F0A500').place(x=60, y=165)

    b3003462 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1LtlYRfsCG3HcEiEklffD7mwuis6WvGXd/view'), text="  اللغة الانكليزية",
                      bg='#F0A500').place(x=60, y=205)

    b4003452 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1cuDkZJ7gp9BKEm-9u3QOdtwwkWQqXUjg/view'), text="    الرياضيات     ",
                      bg='#F0A500').place(x=60, y=245)

    b5003442 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1dxFbexoEZEX9-1i6uxRmvqxblcH_ghE8/view'), text="      الاقتصاد      ",
                      bg='#F0A500').place(x=60, y=285)

    b6003342 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1B2LWWxev5WRmVM6QNK-HGqdO0Iazp_6O/view'), text="      التاريخ        ",
                      bg='#F0A500').place(x=60, y=325)

    b7002324 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1GEpV1AZhCOoVPbc3SqmoMUZHLDMPs3Xr/view'), text="     الجغرافيه      ",
                      bg='#F0A500').place(x=60, y=365)

    b700232 = Button(twfiwin, command=lambda: webbrowser.open('https://drive.google.com/file/d/1EIGdg7Io6AOs1zEgOoWJDq_a_cDkc7pl/view'), text="  نشاط انكليزي  ",
                     bg='#F0A500').place(x=60, y=405)
# ------------------------------------------------------------


# ================================== المتميزين ====================================================


def mtmwin():
    mtmwin = Tk()
    mtmwin.geometry("430x480")
    mtmwin.title("تحميل كتب مدارس المتميزين")
    mtmwin.configure(background='#151D3B')
    mtmwin.resizable(False, False)

    mlm = Label(mtmwin, text='تحميل كتب مدارس المتميزين',  bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=110, y=10)

    lab1 = Label(mtmwin, text='الاول المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=300, y=50)

    bt1 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://static.newton.iq/public/books/files/166.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=website%2F20220327%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220327T152909Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=0c70d5c87897dc255712f58e033c4b70434fe07fa8b9ec6af2ec82eb2825dc41'), bg='#F0A500', text="    الرياضيات     ").place(x=300, y=90)

    bt1 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://static.newton.iq/public/books/files/167.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=website%2F20220327%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220327T152907Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=1080458361f15bdbeba360113186b4e426f4507a8ca5a2f796fd60d9b873f1a9'), bg='#F0A500', text="      الكيمياء       ").place(x=300, y=130)

    bt1 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://static.newton.iq/public/books/files/168.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=website%2F20220327%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220327T152908Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=ae8c2d1396786d0103e71d508a478518ba23cefe2746a291679efcff4a05081c'), bg='#F0A500', text="      الفيزياء       ").place(x=300, y=170)

    bt1 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://static.newton.iq/public/books/files/169.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=website%2F20220327%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220327T152847Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=3c70486e774501e57ee59ec5afb00eec997469e61b98a5e9f9c63031cc8ea5a3'), bg='#F0A500', text="        الاحياء      ").place(x=300, y=210)

# =====================الثاني المتوسط ===========================================

    lab2 = Label(mtmwin, text='الثاني المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=170, y=50)

    bt12 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://static.newton.iq/public/books/files/170.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=website%2F20220327%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220327T154959Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=8d00dbf97b4964d4b040a78aa88d83962897eeb0b486905ddeceafc96832cfba'), bg='#F0A500', text="    الرياضيات     ").place(x=170, y=90)

    bt21 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://static.newton.iq/public/books/files/171.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=website%2F20220327%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220327T154959Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=3c4536f43ee2b4c5e06351592d48cab9a19dabcd4920db0cd301dc8d3b06f191'), bg='#F0A500', text="      الكيمياء       ").place(x=170, y=130)

    bt232 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://static.newton.iq/public/books/files/172.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=website%2F20220327%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220327T155001Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=39f68053543844837ffa7cef0c0d369e7072de6f51c683ddf7125d9136c9584d'), bg='#F0A500', text="      الفيزياء       ").place(x=170, y=170)

    bt221 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://static.newton.iq/public/books/files/173.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=website%2F20220327%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220327T154939Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=2c8147e54552a8682ad828ea09714121bde02299dcd353bc0ba02d170a54f9f9'), bg='#F0A500', text="        الاحياء      ").place(x=170, y=210)

    # ============================ الثالث المتوسط ===============================

    lab3 = Label(mtmwin, text='الثالث المتوسط', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=50)

    bt12 = Button(mtmwin, command=lambda: webbrowser.open(
        'http://manahj.edu.iq/upload/upfile/ar/862.pdf'), bg='#F0A500', text="    الرياضيات     ").place(x=40, y=90)

    bt21 = Button(mtmwin, command=lambda: webbrowser.open(
        'http://manahj.edu.iq/upload/upfile/ar/940.pdf'), bg='#F0A500', text="      الكيمياء       ").place(x=40, y=130)

    bt232 = Button(mtmwin, command=lambda: webbrowser.open(
        'http://manahj.edu.iq/upload/upfile/ar/941.pdf'), bg='#F0A500', text="      الفيزياء       ").place(x=40, y=170)

    bt221 = Button(mtmwin, command=lambda: webbrowser.open(
        'http://manahj.edu.iq/upload/upfile/ar/861.pdf'), bg='#F0A500', text="        الاحياء      ").place(x=40, y=210)

    # =============== الرابع الاعدادي ===============================

    lab4 = Label(mtmwin, text='الرابع الاعدادي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=300, y=280)

    bt12 = Button(mtmwin, command=lambda: webbrowser.open(
        'http://manahj.edu.iq/upload/upfile/ar/866.pdf'), bg='#F0A500', text="    الرياضيات     ").place(x=300, y=320)

    bt21 = Button(mtmwin, command=lambda: webbrowser.open(
        'http://manahj.edu.iq/upload/upfile/ar/865.pdf'), bg='#F0A500', text="      الكيمياء       ").place(x=300, y=360)

    bt232 = Button(mtmwin, command=lambda: webbrowser.open(
        'http://manahj.edu.iq/upload/upfile/ar/867.pdf'), bg='#F0A500', text="      الفيزياء       ").place(x=300, y=400)

    bt221 = Button(mtmwin, command=lambda: webbrowser.open(
        'http://manahj.edu.iq/upload/upfile/ar/864.pdf'), bg='#F0A500', text="        الاحياء      ").place(x=300, y=440)
    # ================== الخامس الاعدادي

    lab5 = Label(mtmwin, text='الخامس احيائي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=160, y=280)

    bt12 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://manahj.edu.iq/upload/upfile/ar/1054.pdf'), bg='#F0A500', text="    الرياضيات     ").place(x=170, y=320)

    bt21 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://manahj.edu.iq/upload/upfile/ar/1052.pdf'), bg='#F0A500', text="      الكيمياء       ").place(x=170, y=360)

    bt232 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://manahj.edu.iq/upload/upfile/ar/1055.pdf'), bg='#F0A500', text="      الفيزياء       ").place(x=170, y=400)

    bt221 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://manahj.edu.iq/upload/upfile/ar/1053.pdf'), bg='#F0A500', text="        الاحياء      ").place(x=170, y=440)

    # =====================================================================
    lab5 = Label(mtmwin, text='الخامس تطبيقي', bg='#151D3B',  fg='white', font=(
        "Tajawl", 13, 'bold')).place(x=40, y=280)

    bt12 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://manahj.edu.iq/upload/upfile/ar/1056.pdf'), bg='#F0A500', text="    الرياضيات     ").place(x=40, y=320)

    bt21 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://manahj.edu.iq/upload/upfile/ar/1057.pdf'), bg='#F0A500', text="      الكيمياء       ").place(x=40, y=360)

    bt232 = Button(mtmwin, command=lambda: webbrowser.open(
        'https://manahj.edu.iq/upload/upfile/ar/1051.pdf'), bg='#F0A500', text="      الفيزياء       ").place(x=40, y=400)


# ****************************************** الشاشه الاولى *********************************
# ليبل الاول
lab1 = Label(firstwin, text="مرحبا بك في تطبيق حقيبة الطالب", bg='#151D3B',
             fg='#F0A500', font=("Tajawl", 20, 'bold')).place(x=150, y=20)

# ليبل الثاني
mainlabel = Label(firstwin, text=": اختر مرحلتك الدراسية", bg='#151D3B',  fg='white', font=(
    "Tajawl", 18)).place(x=420, y=70)


lab2 = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18, 'bold'),  text=": المرحلة الابتدائية").place(x=350, y=120)

btn1 = Button(firstwin, command=thrwin, text="     تحميل الكتب     ",
              bg='#F0A500').place(x=40, y=120)
btn1 = Button(firstwin, command=secwind1, text="     مشاهدة الدروس الالكترونية     ", fg='white', bg='#ab1111').place(
    x=150, y=120)


lab3 = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18, 'bold'),  text=":المرحلة المتوسطة").place(x=350, y=200)

btn1 = Button(firstwin, command=fifwin, text="     تحميل الكتب     ",
              bg='#F0A500').place(x=40, y=200)
btn1 = Button(firstwin, command=forwin, text="     مشاهدة الدروس الالكترونية     ", fg='white', bg='#ab1111').place(
    x=150, y=200)


lab4 = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18, 'bold'),  text=":المرحلة الاعدادية").place(x=360, y=280)
btn1 = Button(firstwin, command=sithwin, text="     تحميل الكتب     ",
              bg='#F0A500').place(x=40, y=280)
btn1 = Button(firstwin, command=sixwin, text="     مشاهدة الدروس الالكترونية     ", fg='white', bg='#ab1111').place(
    x=150, y=280)

lab41 = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18, 'bold'), text=":مدارس المتميزين").place(x=360, y=352)
btn11 = Button(firstwin, command=mtmwin, text="                اضغط هنا لتحميل كتب مدارس المتميزين              ",
               bg='#F0A500').place(x=40, y=360)
# *********************************************************************************************

# ================================= دالة التحميل =======================================

sg = Label(firstwin, bg='#151D3B',  fg='white', font=(
    "Tajawl", 18, 'bold'),  text="   :تحميل الدروس ").place(x=350, y=420)
gg = Button(firstwin, command=lambda: webbrowser.open('https://loader.to/en85/1080p-video-downloader.html'), text="                   اضغط هنا لتحميل الدروس الالكترونية               ", fg='white', bg='#ab1111').place(
    x=40, y=430)


firstwin.mainloop()
