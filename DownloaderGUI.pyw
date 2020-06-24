from __future__ import unicode_literals
from validators import url
from tkinter import *
import youtube_dl
import threading
import os

#https://www.youtube.com/watch?v=YyBYHNjQgrQ

root = Tk()
root.title(" YT Downloader V5.0")
root.geometry("500x250")
root.resizable(False, False)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="resources/ytdl.png"))

def download():

    start_button.config(state=DISABLED)

    if url_stringvar.get() == " Video URL : " or filename.get() == " Desired File Name : ": return None

    try: 
        if url(url_stringvar.get()):
            
            desired_file_name = (filename.get().replace(" ", "_"))

            ydl_opts = {
                "fileformat": "bestaudio/best",
                "outtmpl": f"downloaded_videos/{desired_file_name}.webm",
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url_stringvar.get())

            if desiredformat.get() == 1: os.system(f"ffmpeg -i downloaded_videos/{desired_file_name}.webm {desired_file_name}.mp4")
            elif desiredformat.get() == 2: os.system(f"ffmpeg -i downloaded_videos/{desired_file_name}.webm {desired_file_name}.mp3")
            elif desiredformat.get() == 3: os.system(f"ffmpeg -i downloaded_videos/{desired_file_name}.webm {desired_file_name}.wav")

            os.remove(f"downloaded_videos/{desired_file_name}.webm")

            start_button.config(state=NORMAL)

        else: return start_button.config(state=NORMAL)

    except: start_button.config(state=NORMAL)

def start_buttondownload():
    start_buttonthread = threading.Thread(target=download)
    start_buttonthread.start()

url_stringvar = StringVar(root, value=" Video URL : ")
filename = StringVar(root, value=" Desired File Name : ")

desiredformat = IntVar(root, value=0)

desiredformat.set("1")

title_label = Label(root, text="Youtube Video Downloader V1", font=("Courier", 20))
sentance_entry_label = Label(root, text="Enter Url Here: ")
sentance_entry = Entry(root, textvariable=url_stringvar, width=55)
filename_entry_label = Label(root, text="Enter Desired File Name : ")
filename_entry = Entry(root, textvariable=filename, width=55)
start_button = Button(root, text="Download", width=20, height=5, command=start_buttondownload)
english_language_randiobutton = Radiobutton(root, text="mp4", variable=desiredformat, value=1)
french_language_radiobutton = Radiobutton(root, text="mp3", variable=desiredformat, value=2)
give_examples_checkbutton = Radiobutton(root, text="wav", variable=desiredformat)

title_label.grid(row=1, column=1, columnspan=100, sticky=W, padx=10)
sentance_entry_label.grid(row=2, column=1, sticky=W, padx=10)
sentance_entry.grid(row=2, column=2, sticky=W)
filename_entry_label.grid(row=3, column=1, sticky=W, padx=10)
filename_entry.grid(row=3, column=2, sticky=W)
start_button.grid(row=4, column=1, sticky=W, padx=5)
english_language_randiobutton.grid(row=5, column=1, sticky=W, padx=10)
french_language_radiobutton.grid(row=6, column=1, sticky=W, padx=10)
give_examples_checkbutton.grid(row=7, column=1, sticky=W, padx=10)

if __name__ == "__main__": root.mainloop()
