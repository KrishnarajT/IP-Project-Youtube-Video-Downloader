
"""
This is the IP Project made and programmed in collaboration by:
Krishnaraj Thadesar, Siddharth Jana and Gaurav Sharma

"YOUTUBE VIDEO DOWNLOADER"

Features:
1. Can download any youtube video from the URL
2. Can download the video in either 720p with 360p with Audio
3. Can download only the audio from a video.
4. Can download multiple selected or consecutive videos from a Playlist URL
5. Can save the video in any path of the Computer
6. Can show the progress of the Video that is being downlaoder, and the File size prior to Downloading
7. Has a graphical, intuitive, and easy to use User Interface and Experience
8. Can show data and statistics of the video that you have downloaded.
9. Project is segregated, commented, and organized into functions, classes, and files making it easy to read.
9. Uses Pandas Dataframes to manage the statistics of the user.
10. Can show graphs of the data Collected from the user based on the Videos downloaded.
11. Uses matplotlib to show the graphs to the user.
12. Uses tkinter for the created GUI and python's file management to store the user data.
13. Offers Portability to the user in the form of a single .exe file to download and use.
14. Uses CPU threading for doing longer tasks more efficiently, thereby making the program run faster.
"""

### This is the commented version of the code, Free to edit and change.

### This file is for managing, displaying, downloading and file handling the Downloader.
### refer Readme.md for further details on the project, hierarchy, management and installation of the Project.

## Importing modules

import tkinter as tk # for GUI
from tkinter import ttk # another class from Tkinter for GUI
import pytube as pt # for downloading Youtube Videos
import urllib.request  # for downloading the thumbnails of Youtube Vidoes
import requests # for checking if the Playlist and the URL are valid links
import os # for file management
from tkinter.filedialog import askopenfilename # for opening file dialog box
from PIL import ImageTk, Image # for showing the images in the 
import threading # for multi tasking in the program
import Tags # for oparting youtube tags
import re # for managing youtube regex and compiling playlists.


## defining Some constants

HEIGHT = 720
WIDTH = 1280

TYPE = 'SINGLE'
URL = ''
filesize = 0
maxbytes = 0

INTRO_BGIMG = "Assets/Background Images/INTRO BGIMG.png"
VIDDOWN_SINGLE_BGIMG = "Assets/Background Images/VIDDOWN SINGLE BGIMG 3.png"
VIDDOWN_MULTIPLE_BGIMG = "Assets/Background Images/VIDDOWN MULTIPLE BGIMG.png"
DOWNLOAD_IMAGE = "Assets/Background Images/downloadbtn.png"
REMOVE_IMAGE = "Assets/Background Images/remove.png"
FILE_SELECT_IMAGE = "Assets/Background Images/FILE SELECT1.png"
RESTART_IMAGE = 'Assets/Background Images/onemore.png'
PROCEED_BTN = 'Assets/Background Images/PROCEED BTN.png'
FILENAME = os.getcwd()


play_again = True
download_list = []

sel_stream = '360p'

"""Class to store basic functions that can be used throughout for common purposes"""

class General:

    # returns the unique id of the video from the url, this is the id string that is used to name the thumbnail of the vidoes that we donwlaod.
    @staticmethod
    def get_vid_id(url):
        return url[url.index("=") + 1:]

    # Gets the video thumbnail and saves it in the correct folder
    # example : https://www.youtube.com/watch?v=Kx3aQ75ziNQ is the URL provided by the user
    # it scrapes the part till '=' sign, and then saves the thumbnail as Kx3aQ75ziNQ.png
    @staticmethod
    def get_video_tnl(url, tnurl):
        vid_id = General.get_vid_id(url) + '.png' # get the video id, and the add .png to make the file name.
        tnl = urllib.request.urlretrieve(tnurl, os.path.join('Assets/Thumbnails', vid_id)) # download the thumbnail of the video, and name it vid_id
        return tnl

    # Converts the lengths of the videos from seconds to displayable and understandable formats using basic string manipulation
    # example = length = 139472 seconds, returns 38:59:42 seconds as the length of the video.
    @staticmethod
    def conv_len(length):
        print(length) # the length of the video is given to us in seconds.
        minutes_or_hours = length // 60 # the minutes are the seconds divided by 60 and so on
        if minutes_or_hours < 60:
            print(minutes_or_hours)
            minutes = minutes_or_hours
            seconds = length - (60 * minutes)
            if minutes < 10:
                vid_len = '00:0' + str(minutes) + ':' + str(seconds)
            else:
                vid_len = '00:0' + str(minutes) + ':' + str(seconds)
            return vid_len
        else:
            print(minutes_or_hours)
            hours = minutes_or_hours // 60
            print('hours', hours)
            minutes = (minutes_or_hours - (60 * hours))
            our_seconds = hours * 3600 + minutes * 60
            seconds = length - our_seconds
            if minutes < 10 and seconds < 10:
                vid_len = str(hours) + ':0' + str(minutes) + ':0' + str(seconds)
            elif minutes < 10 and seconds > 10:
                vid_len = str(hours) + ':0' + str(minutes) + ':' + str(seconds)
            else:
                vid_len = str(hours) + ':' + str(minutes) + ':' + str(seconds)

            return vid_len


'''Class that has functions for displaying windows and doing all the work in the program'''

class window:

    # function to show the introduction window, for the user to paste the URL, which gets assigned to the global variable URL.
    # it then checks the URL given by the user to see if it is a single video, or a playlist.
    # if the URL is for a single video, the global variable TYPE is changed to 'single', and if it is a playlist, it is changed to 'PLAYLIST'
    @staticmethod
    def intro_win():
        
        global TYPE # this is required as we want to change the value of the TYPE variable.
        
        
        # this function is called when the Proceed button is pressed by the user.
        def proceed():
            global TYPE, URL
            user_url = entry.get() # gets the URL from the Text box
            r = requests.get(user_url)  # accesses the URL from the net and checks if it is valid
            
            # if the video is not available, then the TYPE is set to invalid
            if "Video unavailable" in r.text:
                print('video is invalid')
                TYPE = 'invalid'
            
            # if the video is valid however, then check if it is a playlist
            else:
                if 'list=' in user_url:
                    TYPE = 'PLAYLIST' # if its a playlist, then assign the TYPE to Playlist
                    print('its a playlist')
                else:
                    TYPE = 'SINGLE'
                print('this is the url', user_url)
                URL = user_url # assign the user_url that we got from the text box to the Global variable URL


        ## Starting a tkinter loop from here, which means this part of the code keeps repeating, and shows the window
        
        root = tk.Tk() # define a root Tk() object
        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH) # create a convas to put photos and text on
        canvas.pack()

        # Placing the background image in the canvas
        BG_IMG = tk.PhotoImage(file=INTRO_BGIMG)
        BG_IMG_LABEL = tk.Label(canvas, image=BG_IMG)
        BG_IMG_LABEL.place(relwidth=1, relheight=1)

        # placing the entry box for entering the url
        entry = tk.Entry(canvas, bg='white', font=("Calibre", 13))
        entry.place(rely=0.80, relx=0.24, relwidth=0.55, relheight=0.05) #  setting the exact position on the screen.

        # declaring the proceed button.
        proceed_img = Image.open(PROCEED_BTN)
        proceed_img = proceed_img.resize((141, 43), Image.ANTIALIAS)
        proceed_img = ImageTk.PhotoImage(proceed_img)

        # placing the proceed button, that calls the proceed function
        proceed_btn = tk.Button(canvas, image=proceed_img, command=lambda: [proceed(), root.destroy()], # checks if the button is pressed
                                bg='#64A8E8', border=0, activebackground='#64A8E8') # if it is pressed, it calls the proceed() function.
        proceed_btn.place(rely=0.9, relx=0.45)

        root.mainloop() # ends the loop if the proceed button is pressed with the destroy() function above.

    # this window shows you the thumbnail of the video along with its title and available qualities, also shows you the
    # download button and the file path selection menu. You click download and the video downloads
    @staticmethod
    def sel_download_win_single(url, video_obj):

        # getting information about the video from the video_object.
        tnurl = video_obj.thumbnail_url
        length = video_obj.length
        title = video_obj.title
        
        
        global play_again, sel_stream

        # on change dropdown value, and link to the main menu
        def change_dropdown(*args):
            
            global sel_stream # this is the stream that the user selects.
            
            sel_stream = tkvar.get() # gets the option from the dropdown that the user selects. example : 720p
            
            video_type = video_obj.streams.get_by_itag(
                list(Tags.tags.keys())[list(Tags.tags.values()).index(sel_stream)]) # declares a video_type object that has the selected stream
            
            mbytes = (round(video_type.filesize / 1000000, 2)).__str__() + ' MB' # gets the file size, because now we know the stream type

            file_size_lbl.config(text=mbytes.__str__()) # print the file size on the screen.

        # opens the file explorer window to select the folder to download, and changes the global file path variable
        def open_file_explorer():
            global FILENAME
            tk.Tk().withdraw()
            FILENAME = tk.filedialog.askdirectory()
            print(FILENAME)
            file_path.config(text=FILENAME) # changes the file path to the one that you selected, and then displays it on the screen.

        # to show the green progess bar, and update the values of the percentage downloaded
        def on_progress_dothis(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
            Bytes = maxbytes - bytes_remaining
            percent = round((100 * (maxbytes - bytes_remaining)) / maxbytes, 2)
            downloading = percent.__str__() + '%'
            progress_bar["value"] = Bytes
            progress_value.config(text=downloading)
            root.update_idletasks()
            if percent == 100.0:
                downloading = 'Done! '
                progress_value.config(text=downloading)

        # to download the video, part of the threading process, then calls the on_progress_do_this() function
        def download():
            global maxbytes
            print("Accessing YouTube URL...")
            video = pt.YouTube(url, on_progress_callback=on_progress_dothis)
            video_type = video.streams.get_by_itag(
                list(Tags.tags.keys())[list(Tags.tags.values()).index(sel_stream)])
            print("Fetching")
            maxbytes = video_type.filesize
            mbytes = (round(video_type.filesize / 1000000, 2)).__str__() + ' MB'
            print(mbytes)
            file_size_lbl.config(text=mbytes.__str__())
            progress_bar["maximum"] = maxbytes
            print(maxbytes)
            video_type.download(FILENAME)

        # quits the window, after changing some global variables
        def restart():
            global play_again
            play_again = True
            root.destroy()
            pass

        # Starting the loop
        root = tk.Tk()
        tkvar = tk.StringVar(root)
        print(tkvar)

        # Defining some image variables to be used in the buttons and the thumbnails

        dimg = Image.open(DOWNLOAD_IMAGE)
        dimg = dimg.resize((167, 51), Image.ANTIALIAS)
        dimg = ImageTk.PhotoImage(dimg)

        flsimg = Image.open(FILE_SELECT_IMAGE)
        flsimg = flsimg.resize((78, 51), Image.ANTIALIAS)
        flsimg = ImageTk.PhotoImage(flsimg)

        dnimg = Image.open(RESTART_IMAGE)
        dnimg = dnimg.resize((125, 125), Image.ANTIALIAS)
        dnimg = ImageTk.PhotoImage(dnimg)

        BG_IMG = tk.PhotoImage(file=VIDDOWN_SINGLE_BGIMG)

        # Creating the Canvas
        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        # Placing the background image in the canvas
        BG_IMG_LABEL = tk.Label(canvas, image=BG_IMG)
        BG_IMG_LABEL.place(relwidth=1, relheight=1)

        # scrapping the thumbnail from the current video and putting it in some folder
        General.get_video_tnl(url, tnurl)

        img = Image.open(os.path.join('Assets/Thumbnails', General.get_vid_id(url) + '.png'))
        img = img.resize((283, 160), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        # displaying the thumbnail
        video_tnl = tk.Label(canvas, image=img)
        video_tnl.place(relx=0.01, rely=0.2)

        # displaying the title of the video
        vid_title = tk.Label(canvas, text=title, anchor='w', font=(
            "Calibre", 18), bg='white', wraplength=800)
        vid_title.place(rely=0.2, relx=0.25)

        # displaying the length of the video
        vid_len = General.conv_len(length)
        vid_length = tk.Label(canvas, text=vid_len, anchor='w', font=(
            "Calibre", 18), bg='white', wraplength=400)
        vid_length.place(rely=0.38, relx=0.25)

        # Creating the drop down menu

        qualities = Tags.get_available_qualities_with_obj(video_obj)
        tkvar.set(qualities[0])  # set the default option
        popupMenu = tk.OptionMenu(canvas, tkvar, *qualities)
        popupMenu.place(relx=0.3, rely=0.52, relwidth=0.2, relheight=0.05)
        tkvar.trace('w', change_dropdown)

        # Displaying the download button
        down_btn = tk.Button(canvas, image=dimg, command=lambda: threading.Thread(target=download).start(),
                             font=("Calibre", 16), bg='white', border=0, activebackground='white')
        down_btn.place(rely=0.9, relx=0.85)

        # displaying the file selection button
        file_selection_btn = tk.Button(canvas, image=flsimg, command=open_file_explorer, font=(
            "Calibre", 16), bg='white', border=0, activebackground='white')
        file_selection_btn.place(rely=0.6, relx=0.25)

        # displaying the file path text box
        file_path = tk.Label(canvas, text=FILENAME, font=("Calibre", 18, 'italic'), bg='white', )
        file_path.place(rely=0.68, relx=0.25)

        progress_bar = ttk.Progressbar(canvas, orient="horizontal", length=200, mode="determinate")
        progress_bar.place(rely=0.82, relx=0.05, relwidth=0.7, relheight=0.05)
        progress_bar['value'] = 0

        # displaying the amount of video downlaoded
        progress_value = tk.Label(canvas, text='', font=("Calibre", 18), bg='white')
        progress_value.place(rely=0.895, relx=0.25)

        # displaying the file size
        file_size_lbl = tk.Label(canvas, text="0 MB", font=("Calibre", 19), bg='white')
        file_size_lbl.place(rely=0.525, relx=0.8)

        # displaying the button for downloading another video, that is restarting the program
        next_btn = tk.Button(canvas, image=dnimg, command=restart, font=("Calibre", 16), bg='#8CB0FF', border=0,
                             activebackground='#8CB0FF')
        next_btn.place(rely=0.01, relx=0.9)
        root.mainloop()

    # this function works basically just like the other function, but for playlists. So there is a bit of extra tkinter elements.
    @staticmethod
    def sel_downlaod_win_playlist(url, playlist_obj):

        global download_list
        """
        this window shows you the thumbnail of the video along with its title and available qualities, also shows you the
        download button and the file path selection menu. You click download and the video downloades.
        """
        download_list = playlist_obj.video_urls
        video_obj = pt.YouTube(download_list[0])
        total_vids = len(playlist_obj.video_urls)

        tnurl = video_obj.thumbnail_url
        cur_video_length = video_obj.length
        cur_video_title = video_obj.title
        global play_again, sel_stream, filesize

        # on change dropdown value, and link to the main menu
        def change_dropdown(*args):
            global sel_stream
            sel_stream = tkvar.get()
            print('value of the sel stream is : ', sel_stream)
            video_type = video_obj.streams.get_by_itag(
                list(Tags.tags.keys())[list(Tags.tags.values()).index(sel_stream)])
            mbytes = (round(video_type.filesize / 1000000, 2)).__str__() + ' MB'
            print(mbytes)
            file_size_lbl.config(text=mbytes.__str__())

        # opens the file explorer window to select the folder to download, and changes the global file path variable
        def open_file_explorer():
            global FILENAME
            tk.Tk().withdraw()
            FILENAME = tk.filedialog.askdirectory()
            print(FILENAME)
            file_path.config(text=FILENAME)

        # to show the progess bar, and update the values of the percentage downloaded
        def on_progress_dothis(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
            Bytes = maxbytes - bytes_remaining
            percent = round((100 * (maxbytes - bytes_remaining)) / maxbytes, 2)
            downloading = percent.__str__() + '%'
            progress_bar["value"] = Bytes
            progress_value.config(text=downloading)
            root.update_idletasks()
            if percent == 100.0:
                downloading = 'Done! '
                progress_value.config(text=downloading)

        # to download the video, part of the threading process, then calls the on_progress_do_this() function
        def download():
            global maxbytes, total_vids
            total_vids = len(download_list)
            downloaded = 0
            skipped = 0
            print(len(download_list))
            for vids in download_list:
                print("Accessing YouTube URL...")
                vid = pt.YouTube(vids, on_progress_callback=on_progress_dothis)
                video_type = vid.streams.get_by_itag(
                    list(Tags.tags.keys())[list(Tags.tags.values()).index(sel_stream)])

                General.get_video_tnl(vid.watch_url, vid.thumbnail_url)
                img1 = Image.open(os.path.join('Assets/Thumbnails',
                                               General.get_vid_id(vid.watch_url) + '.png'))
                img1 = img1.resize((283, 160), Image.ANTIALIAS)
                img1 = ImageTk.PhotoImage(img1)

                cur_vid_length = vid.length
                vid_len1 = General.conv_len(cur_vid_length)
                cur_vid_title = vid.title

                vid_title.config(text=cur_vid_title)
                vid_length.config(text=vid_len1)
                video_tnl.config(image=img1)

                print("Fetching")
                maxbytes = video_type.filesize
                mbytes = (round(video_type.filesize / 1000000, 2)).__str__() + ' MB'
                print(mbytes)
                file_size_lbl.config(text=mbytes.__str__())
                progress_bar["maximum"] = maxbytes
                print(maxbytes)
                video_type.download(FILENAME)
                downloaded += 1
                downloaded_lbl.config(text=downloaded.__str__())
                remaining = total_vids - downloaded
                remaining_lbl.config(text=remaining)
                skipped_lbl.config(text=skipped)
        # quits the window, after changing some global variables

        def restart():
            global play_again
            play_again = True
            root.destroy()
            pass

        def remove():
            """used to remove the selected things from the menu of showing videos"""
            global download_list
            print('you clicked rmeove')
            for item in reversed(all_videos.curselection()):
                all_videos.delete(item)
            download_list = []
            download_list = all_videos.get(0, "end")
            print(download_list)
            remaining_lbl.config(text=len(download_list))
            total_vids_lbl.config(text=len(download_list))

        # Starting the loop
        root = tk.Tk()
        tkvar = tk.StringVar(root)
        print(tkvar)
        # Defining some image variables to be used in the buttons and the thumbnails

        dimg = Image.open(DOWNLOAD_IMAGE)
        dimg = dimg.resize((167, 51), Image.ANTIALIAS)
        dimg = ImageTk.PhotoImage(dimg)

        rimg = Image.open(REMOVE_IMAGE)
        rimg = rimg.resize((170, 30), Image.ANTIALIAS)
        rimg = ImageTk.PhotoImage(rimg)

        flsimg = Image.open(FILE_SELECT_IMAGE)
        flsimg = flsimg.resize((60, 40), Image.ANTIALIAS)
        flsimg = ImageTk.PhotoImage(flsimg)

        dnimg = Image.open(RESTART_IMAGE)
        dnimg = dnimg.resize((125, 125), Image.ANTIALIAS)
        dnimg = ImageTk.PhotoImage(dnimg)

        BG_IMG = tk.PhotoImage(file=VIDDOWN_MULTIPLE_BGIMG)

        # Creating the Canvas
        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        # Placing the background image in the canvas
        BG_IMG_LABEL = tk.Label(canvas, image=BG_IMG)
        BG_IMG_LABEL.place(relwidth=1, relheight=1)

        # scrapping the thumbnail from the current video and putting it in some folder
        General.get_video_tnl(video_obj.watch_url, tnurl)

        # creating the image object for the thumbnails
        img = Image.open(os.path.join('Assets/Thumbnails',
                                      General.get_vid_id(video_obj.watch_url) + '.png'))
        img = img.resize((283, 160), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        # displaying the thumbnail
        video_tnl = tk.Label(canvas, image=img)
        video_tnl.place(relx=0.01, rely=0.2)

        # displaying the title of the video
        vid_title = tk.Label(canvas, text=cur_video_title, anchor='w',
                             font=("Calibre", 18), bg='white', wraplength=800)
        vid_title.place(rely=0.2, relx=0.25)

        # displaying the length of the video
        vid_len = General.conv_len(cur_video_length)
        vid_length = tk.Label(canvas, text=vid_len, anchor='w', font=(
            "Calibre", 18), bg='white', wraplength=400)
        vid_length.place(rely=0.38, relx=0.25)

        # Creating the drop down menu
        qualities = Tags.get_available_qualities_with_obj(video_obj)
        tkvar.set(qualities[0])  # set the default option
        popupMenu = tk.OptionMenu(canvas, tkvar, *qualities)
        popupMenu.place(relx=0.55, rely=0.395, relheight=0.05)
        tkvar.trace('w', change_dropdown)

        # Displaying the download button
        down_btn = tk.Button(canvas, image=dimg, command=lambda: threading.Thread(
            target=download).start(), font=("Calibre", 16), bg='white', border=0, activebackground='white')
        down_btn.place(rely=0.9, relx=0.85)

        # displaying the file selection button
        file_selection_btn = tk.Button(canvas, image=flsimg, command=open_file_explorer, font=(
            "Calibre", 16), bg='white', border=0, activebackground='white')
        file_selection_btn.place(rely=0.38, relx=0.92)

        remove_btn = tk.Button(canvas, image=rimg, command=remove, font=(
            "Calibre", 16), bg='white', border=0, activebackground='white')
        remove_btn.place(rely=0.8, relx=0.02)

        # displaying the file path text box
        file_path = tk.Label(canvas, text=FILENAME, font=("Calibre", 18, 'italic'), bg='white', )
        file_path.place(rely=0.85, relx=0.10)

        # Displaying the scrollbar next to the thing
        scrollbar = tk.Scrollbar(root)
        scrollbar.place(rely=0.53, relx=0.67, relheight=0.25)

        # displaying the listbox
        all_videos = tk.Listbox(canvas, yscrollcommand=scrollbar.set, width=70, font=("Calibre", 16, 'italic'), height=7,
                                selectmode=tk.EXTENDED)
        for video in download_list:
            all_videos.insert(tk.END, video)
        all_videos.place(rely=0.533, relx=0.02)
        scrollbar.config(command=all_videos.yview)

        # displaying the progressbar from downlaoding the current video
        progress_bar = ttk.Progressbar(canvas, orient="horizontal", length=200, mode="determinate")
        progress_bar.place(rely=0.915, relx=0.15, relwidth=0.6, relheight=0.03)
        progress_bar['value'] = 0

        # displaying the amount of video downlaoded
        progress_value = tk.Label(canvas, text='0 %', font=("Calibre", 19), bg='white')
        progress_value.place(rely=0.91, relx=0.76)

        # displaying the file size
        file_size_lbl = tk.Label(canvas, text="0 MB", font=("Calibre", 19), bg='white')
        file_size_lbl.place(rely=0.815, relx=0.88)

        # displaying the number of videos that we skipped coz they were unavailable to download due to some reason or error
        skipped_lbl = tk.Label(canvas, text="0", font=("Calibre", 19), bg='white')
        skipped_lbl.place(rely=0.75, relx=0.92)

        # displaying the remaining number of videos from the selected ones
        remaining_lbl = tk.Label(canvas, text=total_vids, font=("Calibre", 19), bg='white')
        remaining_lbl.place(rely=0.69, relx=0.92)

        # displaying the number of videos that we finished downloading
        downloaded_lbl = tk.Label(canvas, text="0", font=("Calibre", 19), bg='white')
        downloaded_lbl.place(rely=0.63, relx=0.92)

        # displaying whichth number of video it is that we are downloading from our selected list
        cur_number_lbl = tk.Label(canvas, text="0", font=("Calibre", 19), bg='white')
        cur_number_lbl.place(rely=0.57, relx=0.92)

        # displaying the total number of videos in the playlist given by the user
        total_vids_lbl = tk.Label(canvas, text=total_vids, font=("Calibre", 19), bg='white')
        total_vids_lbl.place(rely=0.51, relx=0.92)

        # displaying the button for downloading another video, that is restarting the program
        next_btn = tk.Button(canvas, image=dnimg, command=restart, font=("Calibre", 16), bg='#8CB0FF', border=0,
                             activebackground='#8CB0FF')
        next_btn.place(rely=0.01, relx=0.9)
        root.mainloop()


## Function to run all the things. Function to return to. Function that calls. Function that manages.

def main():
    global play_again # play again is defined globally, and to access it we need to say global play_again
    
    while play_again: # while play_again is true, we should keep running the program again and again
        
        play_again = False # make it False so the loop doesn't run unless the user specifically makes it True
        window.intro_win()  # gets the URL and assigns it to the global vairable URL also checks if the type of the url is a single video,
        # or a playlist and then assigns that to the global variable TYPE
        
        
        if TYPE == 'SINGLE': # if the video is a single video, then do these things
            
            # youtube object used to getting info that is common to both single and playlist downlaods
            yt = pt.YouTube(URL) # this creates an object of the Youtube Class, that has all the information about our playlist.
            window.sel_download_win_single(URL, yt) # now we can call this function to run and display all the things.
            
        else: # if the video is a playlist rather than a single video.
            
            playlist = pt.Playlist(URL) # this is a playlist object of the class Playlist.
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)") # changes the regex of the youtube playlise object
            window.sel_downlaod_win_playlist(URL, playlist) # now we call this function to run display, download and do all the things.

    # as play_again is a global variable, the functions that we called will change the value of the variable if the user presses 'one more'
    # if the user does not press 'one more' then the value of play again remains false, as we assigned the value to be false previously.
    if not play_again: # in which case, say thank you and exit the while loop, thereby exiting the program.
        print('Thanks for using Kappa video downloader')

main() # call the main function.
