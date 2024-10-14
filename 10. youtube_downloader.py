import tkinter
import customtkinter
from pytubefix import YouTube
import os

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        ytVideo = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title)
        finishLabel.configure(text="", text_color="black")
        ytVideo.download("../")
        finishLabel.configure(text=f"Downlaod Complete. File is saved in {os.getcwd()}")
    except Exception as e:
        finishLabel.configure(text="Youtube link is unvalid!", text_color="Red")
        print(e)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = bytes_downloaded / total_size*100
    percent = str(int(percent_completed))
    progressPer.configure(text=f"{percent}%")
    progressPer.update()
    progressBar.set(int(percent)/100)
    progressBar.update()

# system setting
customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("Green")

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

# Progress Bar
progressPer = customtkinter.CTkLabel(app, text="0%")
progressPer.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack()


# Finished Downloading 
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(padx=10, pady=10)

# Run App
app.mainloop()