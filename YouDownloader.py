from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import os

AUDIO_PATH = "./audio"
VIDEO_PATH = "./video"

def init_dirs():
    if not os.path.exists(AUDIO_PATH):
        os.makedirs(AUDIO_PATH)

    if not os.path.exists(VIDEO_PATH):
        os.makedirs(VIDEO_PATH)

def download_audio(yt_url):
    # URL input from user
    yt = YouTube(yt_url)

    # Extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # Check for destination to save file
    #print("Enter the destination (leave blank for current directory)")
    #destination = str(input(">> ")) or '.'
    destination = './audio'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file as .mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    messagebox.showinfo("Complete", yt.title + " AUDIO has been successfully downloaded.")
    url.delete(0, END)

def download_video(yt_url):
    # URL input from user
    yt = YouTube(yt_url)

    # Get the best resolution
    format_options = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    highest_resolution = format_options.first()

    # Check for destination to save file
    destination = './video'

    # Download the file
    highest_resolution.download(output_path=destination)

    # result of success
    messagebox.showinfo("Complete", yt.title + " VIDEO has been successfully downloaded.")
    url.delete(0, END)

def proccess_input():
    yt_url = url.get()
    if option.get() == 0:
        messagebox.showerror("Error","Format no selected")
    elif option.get() == 1:
        download_audio(yt_url)
    elif option.get() == 2:
        download_video(yt_url)
    
    option.set(0)

# Main Programm
root = Tk()
init_dirs()

#App config
root.title("You Downloader")     #Title
root.iconbitmap("./logo.ico")    #Icon
path = 0
if os.name == 'nt':
    path = os.getcwd() + '\\'
else:
    path = os.getcwd() + '/'

#App variables
option = IntVar()
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
button.config(bd=5, font="Curier 12", width=8, height=1, command=lambda:proccess_input())
button.grid(row=1,column=2,padx=5,pady=5)

#Footer label
label_footer = Label(root,)
label_footer.config(font="Curier 10", height=2)
label_footer.grid(row=3, column=0, columnspan=2,padx=5, pady=5)

#Loop of window
root.mainloop()