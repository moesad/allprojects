from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


folder_name = ""


def Mone():
    # file location
    def openlocation():
        global folder_name
        folder_name = filedialog.askdirectory()
        if (len(folder_name) > 1):
            locationError.config(text=folder_name, fg="green")

        else:
            locationError.config(text="اختر الملف", fg="red")

    # donwload video

    def DownloadVideo():
        choice = ytdchoices.get()
        ur1 = ytdEntry.get()
    try:
        if (len(ur1) > 1):
            ytdError.config(text="")
            yt = YouTube(ur1)

            if (choice == choices[0]):
                select = yt.streams.filter(progressive=True). first()

            elif (choice == choices[1]):
                select = yt.streams.filter(
                    progressive=True, file_extension='mp4').last()

            elif (choice == choices[2]):
                select = yt.streams.filter(only_audio=True).first()
    except:
            ytdError.config(text="الرابط مجددا", fg="red")

    # download fucation

        select.download(folder_name)
        ytdError.config(text=" التحميل اكتمل", font=("Tajawl", 15))
        ytdError.place(x=260, y=340)

    root = Tk()

    root.title('V1.1 Youtube Downloader')
    root.geometry("650x410+340+10")
    root.resizable(False, False)
    root.columnconfigure(0, weight=1)

    f1 = Frame(root, width=580, height=100,
               bg="whitesmoke", bd=3, relief=GROOVE)
    f1.place(x=30, y=130)

    f2 = Frame(root, width=580, height=55,
               bg="whitesmoke", bd=3, relief=GROOVE)
    f2.place(x=30, y=250)

    t = Label(root, text="Youtube Downloader  ", bg="red",
              fg='white', font=("Tajawal", 15, 'bold'))
    t.pack(fill=X)
    ytdlabel = Label(root, text="ادخل رابط الفيديو",
                     font=("Tajawal", 15, 'bold'))
    ytdlabel.pack()

    ytdEntryvar = StringVar()
    ytdEntry = Entry(root, width=70, justify='center', font=(
        'Tajawal', 15), fg='blue', textvariable=ytdEntryvar)
    ytdEntry.pack()

    # Error msg

    ytdError = Label(root, text=" ", fg='red', font=('Tajawal', 10))
    ytdError.pack()

    # ask save
    savelabel = Label(root, text="اختر مكان الحفظ",
                      bg="whitesmoke", font=("Tajawal", 15, "bold"))
    savelabel.place(x=450, y=140)

    # btn of save file

    saveEntry = Button(root, width=20, font=(
        "Tajawal", 12), bg="blue", fg="white", text="حدد المسار", command=openlocation)
    saveEntry.place(x=410, y=180)

    # error msg location
    locationError = Label(root, text="اختر مجددا", bg="whitesmoke", fg="red")
    locationError.place(x=100, y=190)

    # download quilty
    ytdquilty = Label(root, text="جودة التحميل",
                      bg="whitesmoke", font=("Tajawal", 15))
    ytdquilty.place(x=430, y=260)

    choices = ['720', '144', "only_audio "]
    ytdchoices = ttk.Combobox(root, values=choices)
    ytdchoices.place(x=260, y=265)

    downloadbtn = Button(root, text="بدا التحميل ", width=20, font=(
        'Tajawal'), bg='green', fg='whitesmoke', command=DownloadVideo)
    downloadbtn.place(x=40, y=260)

    # names label
    x = Label(root, text="Developed by:")
    x.place(x=20, y=350)
    x1 = Label(root, text="Mohammed Sadiq")
    x1.place(x=20, y=370)
    x4 = Label(root, text="TeamX")
    x4.place(x=570, y=340)
    x2 = Label(root, text="Python bootCamp")
    x2.place(x=540, y=360)
    x3 = Label(root, text="2021/11/6")
    x3.place(x=560, y=380)

    root.mainloop()


Mone()
# c = input(" enter: ")
# while True:
#     if c == "n":
#         break
#     else:
#         Mone()
