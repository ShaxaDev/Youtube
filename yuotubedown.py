from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('600x200')
root.title('Youtube Video Downloader')
root.resizable()
Label_1=Label(root,text="Video manzilini kiriting...", font=("bold",20))
Label_1.place(x=120,y=20)

Label_2=Label(root, text="YouTubedagi kichik hajmdagi videolarni\nkompyuterga yuklab olish uchun mo`ljallangan dastur\npython dasturlash tilida yaratildi\n</Developed By: ShaxaDev 2020 ", width=80, font=("bold",9))
Label_2.place(x=140,y=150)

mylink = StringVar()

pastelink = Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140, y=80)


def downloadVideo():
    x = str(mylink.get())
    ytvideo = YouTube(x).streams.filter(
        progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('./YouTubeVideo'):
        os.makedirs('./YouTubeVideo')
    ytvideo.download('./YouTubeVideo')

Button(root,text="Download Video", width=20, bg='green',fg="white", command=downloadVideo).place(x=220, y=110)

root.mainloop()
