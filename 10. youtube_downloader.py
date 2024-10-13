import tkinter
import customtkinter
from pytubefix import YouTube
import os

def startDownload():
    try:
        ytLink = link.get()
        print(ytLink)
        ytObject = YouTube(ytLink)
        ytVideo = ytObject.streams.get_highest_resolution()
        ytVideo.download()
        print(f"Downlaod Complete. File is saved in {os.getcwd()}")
    except Exception as e:
        print(e)

# system setting
customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("Sweet-Blue-Filled")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI element
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx=10, pady=10)

# Adding Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Downlaod", command=startDownload)
download.pack()

# Run App
app.mainloop()