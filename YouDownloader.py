from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import os
import pytube

def convert_to_audio(file):
    name = os.path.basename(file)[:-4]

    #Paths
    location = name + '.mp4'
    renametomp3 = name + '.mp3'

    #Paths for terminal
    location = f"\"{location}\""
    renametomp3 = f"\"{renametomp3}\"" 

    if os.name == 'nt':
        os.system('ren {0} {1}'. format(location, renametomp3))
    else:
        os.system('mv {0} {1}'. format(location, renametomp3))

#Download function
def download():
    if not url.get().startswith("https://"): 
        messagebox.showerror("Error","Invalid link")
        return
    
    #Download
    if option.get() == 1:
        audio = YouTube(url.get())
        stream = audio.streams.filter(only_audio=True)
        audio_file = stream[0].download()

        convert_to_audio(audio_file)  
    else:
        video = YouTube(url.get())
        stream = video.streams.get_highest_resolution()
        stream.download()

def check_input():
    if option.get() == 0:
        messagebox.showerror("Error","Format no selected")
    else:
        download()
        option.set(0)



root = Tk()

#App config
root.title("You Downloader")     #Title
root.iconbitmap("./logo.ico")    #Icon
path = 0
if os.name == 'nt':
    path = os.getcwd() + '\\'
else:
    path = os.getcwd() + '/'

#App variables
option = IntVar();
option.set(0)

#Title label
label_title = Label(root, text = "You Downloader")
label_title.config(font="Curier 20", height=2)
label_title.grid(row=0, column=0, columnspan=2,padx=5, pady=5)

#URL input
url = Entry(root)
url.config(font="Curier 14", width=50)
url.grid(row=1,column=0,padx=5,pady=5)

#Radio Buttons
Radiobutton(root, text="Audio", variable=option, value=1).grid(row=1,column=1,padx=5)
Radiobutton(root, text="Video", variable=option, value=2).grid(row=2,column=1,padx=5)

#Start Button
button = Button(root, text="Download")
button.config(bd=5, font="Curier 12", width=8, height=1, command=lambda:check_input())
button.grid(row=1,column=2,padx=5,pady=5)

#Footer label
label_footer = Label(root,)
label_footer.config(font="Curier 10", height=2)
label_footer.grid(row=3, column=0, columnspan=2,padx=5, pady=5)

#Loop of window
root.mainloop()