# This python app sort all files of Download folder in different folders based on its extension.

import os

home = os.environ.get("HOME") 
os.chdir(home)

folder_list = ["Documents", "Music", "Pictures", "Videos", "Uncatagorized"]


#check if all folder are present.
for folder in folder_list:
    print(f"{folder} : {folder in os.listdir()}")
    if (folder not in os.listdir()):
        os.mkdir(f"{folder}")
        print(f"{folder} is created")
    
#Get the list of all files in Downlaods folder
os.chdir("Downloads")
file_list = [file for file in os.listdir() if os.path.isfile(file)]


""" check extensions of each file to understand where it goes """

doc_lst = ['.csv', '.pdf', '.xlsx', '.docx', '.doc', '.txt']

audio_lst = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', 
            '.awb', '.dss', '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p',
            '.mmf', '.movpkg', '.mp3', '.mpc', '.msv', '.nmf', '.ogg', '.oga', '.mogg', '.opus', 
            '.ra', '.rm', '.raw', '.rf64', '.sln', '.tta', '.voc', '.vox', '.wav', '.wma', '.wv', 
            '.webm', '.8svx', '.cda']

image_lst = ['.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.gif', '.png', 'jp2', '.j2k', '.jpf', 
             '.jpm', '.jpg2', '.j2c', '.jpc', '.jpx', '.mj2', '.webp', '.heif', '.heifs', '.heic', 
             '.heics', '.avci', '.avcs', '.HIF', '.avif', '.avifs', '.jxl', '.tiff', '.tif', '.bmp', 
             '.dib', '.pbm', '.pgm', '.ppm', '.pnm']

video_list = ['.webm', '.mkv', '.flv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.gif', '.gifv', 
              '.mng', '.avi', '.MTS', '.M2TS', '.TS', '.mov', '.qt', '.wmv', '.yuv', '.rm', '.rmvb', 
              '.viv', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', 
              '.mpe', '.mpv', '.mpg', '.mpeg', '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', 
              '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b']



for file in file_list:
    file_name, file_ext = os.path.splitext(file)
    if file_ext in doc_lst:
        os.rename(file,home + "/Documents/"+ os.path.basename(file))
        print(f"{file} is moved in Documents folder") 

    elif file_ext in audio_lst:
        os.rename(file,home + "/Music/"+ os.path.basename(file))
        print(f"{file} is moved in Music folder")

    elif file_ext in image_lst:
        os.rename(file,home + "/Pictures/"+ os.path.basename(file))
        print(f"{file} is moved in Pictures folder")

    elif file_ext in audio_lst:
        os.rename(file,home + "/Videos/"+ os.path.basename(file))
        print(f"{file} is moved in Videos folder")

    else:
        os.rename(file,home + "/Uncatagorized/"+ os.path.basename(file))
        print(f"{file} is moved in Uncatagorized folder")


