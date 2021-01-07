# importing the things
# import os
import os
import tkinter as tk
import time
from tkinter import ttk
import pytube as pt
import requests
from tkinter.filedialog import askopenfilename

import youtube_dl
from PIL import ImageTk, Image
import threading
import Tags
import re
import File_IO as fio
import methods
import Graphs


# defining Some constants

HEIGHT = 720
WIDTH = 1280
TYPE = 'SINGLE'
# INTRO_BGIMG = "C:/Users/littl/Desktop/Programs/Python/Kappa Video Downloader/Assets/Background Images/INTRO BGIMG.png"
INTRO_BGIMG = "Assets/Background Images/INTRO BGIMG.png"
VIDDOWN_SINGLE_BGIMG = "Assets/Background Images/VIDDOWN SINGLE BGIMG 3.png"
VIDDOWN_MULTIPLE_BGIMG = "Assets/Background Images/VIDDOWN MULTIPLE BGIMG.png"
DOWNLOAD_IMAGE = "Assets/Background Images/downloadbtn.png"
REMOVE_IMAGE = "Assets/Background Images/remove.png"
FILE_SELECT_IMAGE = "Assets/Background Images/FILE SELECT1.png"
RESTART_IMAGE = 'Assets/Background Images/onemore.png'
PROCEED_BTN = 'Assets/Background Images/PROCEED BTN.png'
STATISTICS_BTN = 'Assets/Background Images/STATISTICS BTN.png'
URL = ''
FILENAME = os.getcwd()
maxbytes = 0
sth = 1
again = True
done = False
video_titles = []
video_titles_with_urls = []
like_counts = []
dislike_counts = []
Quality_tag = 142
filesize = 0
playlist_URLS = [ ]
download_list = [ ]
sel_stream = '360p'

'''Class that has functions for displaying windows and doing all the work in the program'''

class window :
    
    @staticmethod
    def intro_win() :
        """
        function that displays the introduction tkinter window, and has enter button that closes it.
        Also checks if the link is a playlist or a single video, and if it is, then it changes the
        type from single to playlist it then returns the url of the video
        """
        
        global TYPE
        
        # checks if the url is valid, changes the global volues.
        def proceed() :
            global TYPE, URL
            user_url = entry.get()
            r = requests.get( user_url )  # random video id
            if "Video unavailable" in r.text :
                print( 'video is invalid' )
                TYPE = 'invalid'
            else :
                if 'list=' in user_url :
                    TYPE = 'PLAYLIST'
                    print( 'its a playlist' )
                else :
                    TYPE = 'SINGLE'
                print( 'this is the url', user_url )
                URL = user_url
        
        # runs if you pressed the statistics button, redirects you to the statistics page.
        def statistics() :
            global TYPE
            TYPE = 'STATISTICS'
        
        # Beginning loop from here
        root = tk.Tk()
        canvas = tk.Canvas( root, height = HEIGHT, width = WIDTH )
        canvas.pack()
        
        # Placing the background image in the canvas
        BG_IMG = tk.PhotoImage( file = INTRO_BGIMG, master = root )
        BG_IMG_LABEL = tk.Label( canvas, image = BG_IMG )
        BG_IMG_LABEL.place( relwidth = 1, relheight = 1 )
        
        # placing the entry box for entering the url
        entry = tk.Entry( canvas, bg = 'white', font = ("Calibre", 13) )
        entry.place( rely = 0.80, relx = 0.24, relwidth = 0.55, relheight = 0.05 )
        
        proceed_img = Image.open( PROCEED_BTN )
        proceed_img = proceed_img.resize( (141, 43), Image.ANTIALIAS )
        proceed_img = ImageTk.PhotoImage( proceed_img )
        
        statistics_img = Image.open( STATISTICS_BTN )
        statistics_img = statistics_img.resize( (141, 43), Image.ANTIALIAS )
        statistics_img = ImageTk.PhotoImage( statistics_img )
        
        # placing the proceed button, that calls the proceed function
        proceed_btn = tk.Button( canvas, image = proceed_img, command = lambda : [ proceed(), root.destroy() ],
                                 bg = '#64A8E8', border = 0, activebackground = '#64A8E8' )
        proceed_btn.place( rely = 0.9, relx = 0.38 )
        
        # placing the Statistics button, that calls the Statistics window
        statistics_btn = tk.Button( canvas, image = statistics_img, command = lambda : [ statistics(), root.destroy() ],
                                    bg = '#64A8E8', border = 0, activebackground = '#64A8E8' )
        statistics_btn.place( rely = 0.9, relx = 0.51 )
        
        root.mainloop()
    
    # This is the backup
    @staticmethod  # this thing works tho...
    def sel_download_win_single( url, video_obj ) :
        """
        this window shows you the thumbnail of the video along with its title and available qualities, also shows you the
        download button and the file path selection menu. You click download and the video downloades.
        """
        tnurl = video_obj.thumbnail_url
        length = video_obj.length
        # author = video_obj.author
        title = video_obj.title
        global again, sel_stream
        
        # on change dropdown value, and link to the main menu
        def change_dropdown( *args ) :
            global sel_stream
            sel_stream = tkvar.get()
            print( 'value of the sel stream is : ', sel_stream )
            video_type = video_obj.streams.get_by_itag(
                    list( Tags.tags.keys() )[ list( Tags.tags.values() ).index( sel_stream ) ] )
            mbytes = (round( video_type.filesize / 1000000, 2 )).__str__() + ' MB'
            print( mbytes )
            file_size_lbl.config( text = mbytes.__str__() )
        
        # opens the file explorer window to select the folder to download, and changes the global file path variable
        def open_file_explorer() :
            global FILENAME
            tk.Tk().withdraw()
            FILENAME = tk.filedialog.askdirectory()
            print( FILENAME )
            file_path.config( text = FILENAME )
        
        # to show the progess bar, and update the values of the percentage downloaded
        def on_progress_dothis( stream, chunk: bytes, bytes_remaining: int ) -> None :  # pylint: disable=W0613
            Bytes = maxbytes - bytes_remaining
            percent = round( (100 * (maxbytes - bytes_remaining)) / maxbytes, 2 )
            downloading = percent.__str__() + '%'
            progress_bar[ "value" ] = Bytes
            progress_value.config( text = downloading )
            root.update_idletasks()
            if percent == 100.0 :
                downloading = 'Done! '
                progress_value.config( text = downloading )
        
        # to download the video, part of the threading process, then calls the on_progress_do_this() function
        def download() :
            global maxbytes
            print( "Accessing YouTube URL..." )
            video = pt.YouTube( url, on_progress_callback = on_progress_dothis )
            video_type = video.streams.get_by_itag(
                    list( Tags.tags.keys() )[ list( Tags.tags.values() ).index( sel_stream ) ] )
            print( "Fetching" )
            maxbytes = video_type.filesize
            mbytes = (round( video_type.filesize / 1000000, 2 )).__str__() + ' MB'
            print( mbytes )
            file_size_lbl.config( text = mbytes.__str__() )
            progress_bar[ "maximum" ] = maxbytes
            print( maxbytes )
            video_type.download( FILENAME )
        
        # quits the window, after changing some global variables
        def restart() :
            global again
            again = True
            root.destroy()
            pass
        
        # Starting the loop
        root = tk.Tk()
        tkvar = tk.StringVar( root )
        print( tkvar )
        
        # Defining some image variables to be used in the buttons and the thumbnails
        
        dimg = Image.open( DOWNLOAD_IMAGE )
        dimg = dimg.resize( (167, 51), Image.ANTIALIAS )
        dimg = ImageTk.PhotoImage( dimg )
        
        flsimg = Image.open( FILE_SELECT_IMAGE )
        flsimg = flsimg.resize( (78, 51), Image.ANTIALIAS )
        flsimg = ImageTk.PhotoImage( flsimg )
        
        dnimg = Image.open( RESTART_IMAGE )
        dnimg = dnimg.resize( (125, 125), Image.ANTIALIAS )
        dnimg = ImageTk.PhotoImage( dnimg )
        
        BG_IMG = tk.PhotoImage( file = VIDDOWN_SINGLE_BGIMG )
        
        # Creating the Canvas
        canvas = tk.Canvas( root, height = HEIGHT, width = WIDTH )
        canvas.pack()
        
        # Placing the background image in the canvas
        BG_IMG_LABEL = tk.Label( canvas, image = BG_IMG )
        BG_IMG_LABEL.place( relwidth = 1, relheight = 1 )
        
        # scrapping the thumbnail from the current video and putting it in some folder
        methods.get_video_tnl( url, tnurl )
        
        img = Image.open( os.path.join( 'Assets/Thumbnails', methods.get_vid_id( url ) + '.png' ) )
        img = img.resize( (283, 160), Image.ANTIALIAS )
        img = ImageTk.PhotoImage( img )
        
        # displaying the thumbnail
        video_tnl = tk.Label( canvas, image = img )
        video_tnl.place( relx = 0.01, rely = 0.2 )
        
        # displaying the title of the video
        vid_title = tk.Label( canvas, text = title, anchor = 'w', font = (
            "Calibre", 18), bg = 'white', wraplength = 800 )
        vid_title.place( rely = 0.2, relx = 0.25 )
        
        # displaying the length of the video
        vid_len = methods.conv_len( length )
        vid_length = tk.Label( canvas, text = vid_len, anchor = 'w', font = (
            "Calibre", 18), bg = 'white', wraplength = 400 )
        vid_length.place( rely = 0.38, relx = 0.25 )
        
        # Creating the drop down menu
        
        qualities = Tags.get_available_qualities_with_obj( video_obj )
        tkvar.set( qualities[ 0 ] )  # set the default option
        popupMenu = tk.OptionMenu( canvas, tkvar, *qualities )
        popupMenu.place( relx = 0.3, rely = 0.52, relwidth = 0.2, relheight = 0.05 )
        tkvar.trace( 'w', change_dropdown )
        
        # Displaying the download button
        down_btn = tk.Button( canvas, image = dimg, command = lambda : threading.Thread( target = download ).start(),
                              font = ("Calibre", 16), bg = 'white', border = 0, activebackground = 'white' )
        down_btn.place( rely = 0.9, relx = 0.85 )
        
        # displaying the file selection button
        file_selection_btn = tk.Button( canvas, image = flsimg, command = open_file_explorer, font = (
            "Calibre", 16), bg = 'white', border = 0, activebackground = 'white' )
        file_selection_btn.place( rely = 0.6, relx = 0.25 )
        
        # displaying the file path text box
        file_path = tk.Label( canvas, text = FILENAME, font = ("Calibre", 18, 'italic'), bg = 'white', )
        file_path.place( rely = 0.68, relx = 0.25 )
        
        progress_bar = ttk.Progressbar( canvas, orient = "horizontal", length = 200, mode = "determinate" )
        progress_bar.place( rely = 0.82, relx = 0.05, relwidth = 0.7, relheight = 0.05 )
        progress_bar[ 'value' ] = 0
        
        # displaying the amount of video downlaoded
        progress_value = tk.Label( canvas, text = '', font = ("Calibre", 18), bg = 'white' )
        progress_value.place( rely = 0.895, relx = 0.25 )
        
        # displaying the file size
        file_size_lbl = tk.Label( canvas, text = "0 MB", font = ("Calibre", 19), bg = 'white' )
        file_size_lbl.place( rely = 0.525, relx = 0.8 )
        
        # displaying the button for downloading another video, that is restarting the program
        next_btn = tk.Button( canvas, image = dnimg, command = restart, font = ("Calibre", 16), bg = '#8CB0FF', border = 0,
                              activebackground = '#8CB0FF' )
        next_btn.place( rely = 0.01, relx = 0.9 )
        root.mainloop()
    
    @staticmethod
    def sel_downlaod_win_playlist( playlist_obj ) :
        
        global download_list
        """
        this window shows you the thumbnail of the video along with its title and available qualities, also shows you the
        download button and the file path selection menu. You click download and the video downloades.
        """
        download_list = playlist_obj.video_urls
        video_obj = pt.YouTube(download_list[0])
        total_vids = len( playlist_obj.video_urls )
        
        tnurl = video_obj.thumbnail_url
        cur_video_length = video_obj.length
        cur_video_title = video_obj.title
        global again, sel_stream, filesize
        
        # on change dropdown value, and link to the main menu
        def change_dropdown( *args ) :
            global sel_stream
            sel_stream = tkvar.get()
            print( 'value of the sel stream is : ', sel_stream )
            video_type = video_obj.streams.get_by_itag(
                    list( Tags.tags.keys() )[ list( Tags.tags.values() ).index( sel_stream ) ] )
            mbytes = (round( video_type.filesize / 1000000, 2 )).__str__() + ' MB'
            print( mbytes )
            file_size_lbl.config( text = mbytes.__str__() )
        
        # opens the file explorer window to select the folder to download, and changes the global file path variable
        def open_file_explorer() :
            global FILENAME
            tk.Tk().withdraw()
            FILENAME = tk.filedialog.askdirectory()
            print( FILENAME )
            file_path.config( text = FILENAME )
        
        # to show the progess bar, and update the values of the percentage downloaded
        def on_progress_dothis( stream, chunk: bytes, bytes_remaining: int ) -> None :  # pylint: disable=W0613
            Bytes = maxbytes - bytes_remaining
            percent = round( (100 * (maxbytes - bytes_remaining)) / maxbytes, 2 )
            downloading = percent.__str__() + '%'
            progress_bar[ "value" ] = Bytes
            progress_value.config( text = downloading )
            root.update_idletasks()
            if percent == 100.0 :
                downloading = 'Done! '
                progress_value.config( text = downloading )
        
        # to download the video, part of the threading process, then calls the on_progress_do_this() function
        def download() :
            global maxbytes, total_vids
            total_vids = len( download_list )
            downloaded = 0
            skipped = 0
            print( len( download_list ) )
            for vids in download_list :
                print( "Accessing YouTube URL..." )
                vid = pt.YouTube( vids, on_progress_callback = on_progress_dothis )
                video_type = vid.streams.get_by_itag(
                        list( Tags.tags.keys() )[ list( Tags.tags.values() ).index( sel_stream ) ] )
                
                methods.get_video_tnl( vid.watch_url, vid.thumbnail_url )
                img1 = Image.open( os.path.join( 'Assets/Thumbnails',
                                                 methods.get_vid_id( vid.watch_url ) + '.png' ) )
                img1 = img1.resize( (283, 160), Image.ANTIALIAS )
                img1 = ImageTk.PhotoImage( img1 )
                
                cur_vid_length = vid.length
                vid_len1 = methods.conv_len( cur_vid_length )
                cur_vid_title = vid.title
                
                vid_title.config( text = cur_vid_title )
                vid_length.config( text = vid_len1 )
                video_tnl.config( image = img1 )
                
                print( "Fetching" )
                maxbytes = video_type.filesize
                mbytes = (round( video_type.filesize / 1000000, 2 )).__str__() + ' MB'
                print( mbytes )
                file_size_lbl.config( text = mbytes.__str__() )
                progress_bar[ "maximum" ] = maxbytes
                print( maxbytes )
                video_type.download( FILENAME )
                downloaded += 1
                downloaded_lbl.config( text = downloaded.__str__() )
                remaining = total_vids - downloaded
                remaining_lbl.config( text = remaining )
                skipped_lbl.config( text = skipped )
        
        # quits the window, after changing some global variables
        
        def restart() :
            global again
            again = True
            root.destroy()
            pass
        
        def remove() :
            """used to remove the selected things from the menu of showing videos"""
            global download_list
            print( 'you clicked remove' )
            for item in reversed( all_videos.curselection() ) :
                all_videos.delete( item )
            download_list = [ ]
            download_list = all_videos.get( 0, "end" )
            new_list = []
            for i in range(len(download_list)):
                new_list.append(download_list[i][1])
            download_list = new_list
            remaining_lbl.config( text = len( download_list ) )
            total_vids_lbl.config( text = len( download_list ) )
        
        # Starting the loop
        root = tk.Tk()
        tkvar = tk.StringVar( root )
        print( tkvar )
        # Defining some image variables to be used in the buttons and the thumbnails
        
        dimg = Image.open( DOWNLOAD_IMAGE )
        dimg = dimg.resize( (167, 51), Image.ANTIALIAS )
        dimg = ImageTk.PhotoImage( dimg )
        
        rimg = Image.open( REMOVE_IMAGE )
        rimg = rimg.resize( (170, 30), Image.ANTIALIAS )
        rimg = ImageTk.PhotoImage( rimg )
        
        flsimg = Image.open( FILE_SELECT_IMAGE )
        flsimg = flsimg.resize( (60, 40), Image.ANTIALIAS )
        flsimg = ImageTk.PhotoImage( flsimg )
        
        dnimg = Image.open( RESTART_IMAGE )
        dnimg = dnimg.resize( (125, 125), Image.ANTIALIAS )
        dnimg = ImageTk.PhotoImage( dnimg )
        
        BG_IMG = tk.PhotoImage( file = VIDDOWN_MULTIPLE_BGIMG )
        
        # Creating the Canvas
        canvas = tk.Canvas( root, height = HEIGHT, width = WIDTH )
        canvas.pack()
        
        # Placing the background image in the canvas
        BG_IMG_LABEL = tk.Label( canvas, image = BG_IMG )
        BG_IMG_LABEL.place( relwidth = 1, relheight = 1 )
        
        # scrapping the thumbnail from the current video and putting it in some folder
        methods.get_video_tnl( video_obj.watch_url, tnurl )
        
        # creating the image object for the thumbnails
        img = Image.open( os.path.join( 'Assets/Thumbnails',
                                        methods.get_vid_id( video_obj.watch_url ) + '.png' ) )
        img = img.resize( (283, 160), Image.ANTIALIAS )
        img = ImageTk.PhotoImage( img )
        
        # displaying the thumbnail
        video_tnl = tk.Label( canvas, image = img )
        video_tnl.place( relx = 0.01, rely = 0.2 )
        
        # displaying the title of the video
        vid_title = tk.Label( canvas, text = cur_video_title, anchor = 'w',
                              font = ("Calibre", 18), bg = 'white', wraplength = 800 )
        vid_title.place( rely = 0.2, relx = 0.25 )
        
        # displaying the length of the video
        vid_len = methods.conv_len( cur_video_length )
        vid_length = tk.Label( canvas, text = vid_len, anchor = 'w', font = (
            "Calibre", 18), bg = 'white', wraplength = 400 )
        vid_length.place( rely = 0.38, relx = 0.25 )
        
        # Creating the drop down menu
        qualities = Tags.get_available_qualities_with_obj( video_obj )
        tkvar.set( qualities[ 0 ] )  # set the default option
        popupMenu = tk.OptionMenu( canvas, tkvar, *qualities )
        popupMenu.place( relx = 0.55, rely = 0.395, relheight = 0.05 )
        tkvar.trace( 'w', change_dropdown )
        
        # Displaying the download button
        down_btn = tk.Button( canvas, image = dimg, command = lambda : threading.Thread(
                target = download ).start(), font = ("Calibre", 16), bg = 'white', border = 0, activebackground = 'white' )
        down_btn.place( rely = 0.9, relx = 0.85 )
        
        # displaying the file selection button
        file_selection_btn = tk.Button( canvas, image = flsimg, command = open_file_explorer, font = (
            "Calibre", 16), bg = 'white', border = 0, activebackground = 'white' )
        file_selection_btn.place( rely = 0.38, relx = 0.92 )
        
        remove_btn = tk.Button( canvas, image = rimg, command = remove, font = (
            "Calibre", 16), bg = 'white', border = 0, activebackground = 'white' )
        remove_btn.place( rely = 0.8, relx = 0.02 )
        
        # displaying the file path text box
        file_path = tk.Label( canvas, text = FILENAME, font = ("Calibre", 18, 'italic'), bg = 'white', )
        file_path.place( rely = 0.85, relx = 0.10 )
        
        # Displaying the scrollbar next to the thing
        scrollbar = tk.Scrollbar( root )
        scrollbar.place( rely = 0.53, relx = 0.67, relheight = 0.25 )
        
        # displaying the listbox
        all_videos = tk.Listbox( canvas, yscrollcommand = scrollbar.set, width = 70, font = ("Calibre", 16, 'italic'), height = 7,
                                 selectmode = tk.EXTENDED )
        for video in video_titles_with_urls :
            all_videos.insert( tk.END, video )
        all_videos.place( rely = 0.533, relx = 0.02 )
        scrollbar.config( command = all_videos.yview )
        
        # displaying the progressbar from downlaoding the current video
        progress_bar = ttk.Progressbar( canvas, orient = "horizontal", length = 200, mode = "determinate" )
        progress_bar.place( rely = 0.915, relx = 0.15, relwidth = 0.6, relheight = 0.03 )
        progress_bar[ 'value' ] = 0
        
        # displaying the amount of video downlaoded
        progress_value = tk.Label( canvas, text = '0 %', font = ("Calibre", 19), bg = 'white' )
        progress_value.place( rely = 0.91, relx = 0.76 )
        
        # displaying the file size
        file_size_lbl = tk.Label( canvas, text = "0 MB", font = ("Calibre", 19), bg = 'white' )
        file_size_lbl.place( rely = 0.815, relx = 0.88 )
        
        # displaying the number of videos that we skipped coz they were unavailable to download due to some reason or error
        skipped_lbl = tk.Label( canvas, text = "0", font = ("Calibre", 19), bg = 'white' )
        skipped_lbl.place( rely = 0.75, relx = 0.92 )
        
        # displaying the remaining number of videos from the selected ones
        remaining_lbl = tk.Label( canvas, text = total_vids, font = ("Calibre", 19), bg = 'white' )
        remaining_lbl.place( rely = 0.69, relx = 0.92 )
        
        # displaying the number of videos that we finished downloading
        downloaded_lbl = tk.Label( canvas, text = "0", font = ("Calibre", 19), bg = 'white' )
        downloaded_lbl.place( rely = 0.63, relx = 0.92 )
        
        # displaying whichth number of video it is that we are downloading from our selected list
        cur_number_lbl = tk.Label( canvas, text = "0", font = ("Calibre", 19), bg = 'white' )
        cur_number_lbl.place( rely = 0.57, relx = 0.92 )
        
        # displaying the total number of videos in the playlist given by the user
        total_vids_lbl = tk.Label( canvas, text = total_vids, font = ("Calibre", 19), bg = 'white' )
        total_vids_lbl.place( rely = 0.51, relx = 0.92 )
        
        # displaying the button for downloading another video, that is restarting the program
        next_btn = tk.Button( canvas, image = dnimg, command = restart, font = ("Calibre", 16), bg = '#8CB0FF', border = 0,
                              activebackground = '#8CB0FF' )
        next_btn.place( rely = 0.01, relx = 0.9 )
        root.mainloop()
    
    @staticmethod
    def statistics() :
    
        root = tk.Tk()
        root.geometry( "1280x720" )
    
        # Creating the notebook, that enables tabs
        my_notebook = ttk.Notebook( root )
        my_notebook.pack()
    
        # _____________Views Tab_________________#
    
        base_frame_tab_1 = tk.Frame( my_notebook, width = 1280, height = 5000, bg = "#65A8E8" )
    
        # Adding a scrollbar to that tab
        base_canvas_tab_1 = tk.Canvas( base_frame_tab_1, width = 1250, height = 5000 )
        base_canvas_tab_1.pack( side = tk.LEFT, fill = tk.BOTH, expand = 1 )
        my_scrollbar = ttk.Scrollbar( base_frame_tab_1, orient = tk.VERTICAL, command = base_canvas_tab_1.yview )
        my_scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        base_canvas_tab_1.configure( yscrollcommand = my_scrollbar.set )
        base_canvas_tab_1.bind( '<Configure>', lambda e : base_canvas_tab_1.configure( scrollregion = base_canvas_tab_1.bbox( "all" ) ) )
        tab_frame_1 = tk.Frame( base_canvas_tab_1, width = 1280, height = 5000, bg = "#65A8E8" )
        base_canvas_tab_1.create_window( (0, 0), window = tab_frame_1, anchor = "nw" )
    
        # ____Stuff in the tab___#
    
        bg_label_1 = tk.Label( tab_frame_1, text = 'Views Vs Videos Downloaded', bg = '#65A8E8', font = ("Calibre", 30) )
        bg_label_1.place( relx = 0.3, rely = 0.01 )
        views_graph_img = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/views_line_graph.png' ) )
        views_graph_img_lbl = tk.Label( tab_frame_1, image = views_graph_img )
        views_graph_img_lbl.place( relx = 0.25, rely = 0.03 )
        views_graph_img_2 = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/views_bar_graph.png' ) )
        views_graph_img_2_lbl = tk.Label( tab_frame_1, image = views_graph_img_2 )
        views_graph_img_2_lbl.place( relx = 0.25, rely = 0.13 )
        views_graph_img_3 = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/views_hist_graph.png' ) )
        views_graph_img_3_lbl = tk.Label( tab_frame_1, image = views_graph_img_3 )
        views_graph_img_3_lbl.place( relx = 0.25, rely = 0.23 )
    
        # ___#
    
        # _______________Ratings Tab__________________#
    
        base_frame_tab_2 = tk.Frame( my_notebook, width = 1280, height = 5000, bg = "#65A8E8" )
    
        # Adding scrollbar to that tab
        base_canvas_tab_2 = tk.Canvas( base_frame_tab_2, width = 1250, height = 5000 )
        base_canvas_tab_2.pack( side = tk.LEFT, fill = tk.BOTH, expand = 1 )
        my_scrollbar = ttk.Scrollbar( base_frame_tab_2, orient = tk.VERTICAL, command = base_canvas_tab_2.yview )
        my_scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        base_canvas_tab_2.configure( yscrollcommand = my_scrollbar.set )
        base_canvas_tab_2.bind( '<Configure>', lambda e : base_canvas_tab_2.configure( scrollregion = base_canvas_tab_2.bbox( "all" ) ) )
        tab_frame_2 = tk.Frame( base_canvas_tab_2, width = 1280, height = 5000, bg = "#65A8E8" )
        base_canvas_tab_2.create_window( (0, 0), window = tab_frame_2, anchor = "nw" )
    
        # ____Stuff in the tab___#
    
        bg_label_2 = tk.Label( tab_frame_2, text = 'Ratings Vs Videos Downloaded', bg = '#65A8E8', font = ("Calibre", 30) )
        bg_label_2.place( relx = 0.3, rely = 0.01 )
        ratings_graph_img = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/ratings_bar_graph.png' ) )
        ratings_graph_img_lbl = tk.Label( tab_frame_2, image = ratings_graph_img )
        ratings_graph_img_lbl.place( relx = 0.25, rely = 0.03 )
        ratings_graph_img_2 = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/ratings_hist_graph.png' ) )
        ratings_graph_img_2_lbl = tk.Label( tab_frame_2, image = ratings_graph_img_2 )
        ratings_graph_img_2_lbl.place( relx = 0.25, rely = 0.13 )
    
        # ___#
    
        # _______________Tab 3__________________#
    
        base_frame_tab_3 = tk.Frame( my_notebook, width = 1280, height = 5000, bg = "#65A8E8" )
    
        # Adding scrollbar to that tab
        base_canvas_tab_3 = tk.Canvas( base_frame_tab_3, width = 1250, height = 5000 )
        base_canvas_tab_3.pack( side = tk.LEFT, fill = tk.BOTH, expand = 1 )
        my_scrollbar = ttk.Scrollbar( base_frame_tab_3, orient = tk.VERTICAL, command = base_canvas_tab_3.yview )
        my_scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        base_canvas_tab_3.configure( yscrollcommand = my_scrollbar.set )
        base_canvas_tab_3.bind( '<Configure>', lambda e : base_canvas_tab_3.configure( scrollregion = base_canvas_tab_3.bbox( "all" ) ) )
        tab_frame_3 = tk.Frame( base_canvas_tab_3, width = 1280, height = 5000, bg = "#65A8E8" )
        base_canvas_tab_3.create_window( (0, 0), window = tab_frame_3, anchor = "nw" )
    
        # ____Stuff in the tab___#
    
        bg_label_3 = tk.Label( tab_frame_3, text = 'Likes Vs Videos Downloaded', bg = '#65A8E8', font = ("Calibre", 30) )
        bg_label_3.place( relx = 0.3, rely = 0.01 )
        likes_graph_img = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/likes_hist_graph.png' ) )
        likes_graph_img_lbl = tk.Label( tab_frame_3, image = likes_graph_img )
        likes_graph_img_lbl.place( relx = 0.25, rely = 0.03 )
        likes_graph_img_2 = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/likes_line_graph.png' ) )
        likes_graph_img_2_lbl = tk.Label( tab_frame_3, image = likes_graph_img_2 )
        likes_graph_img_2_lbl.place( relx = 0.25, rely = 0.13 )
    
        # ___#
    
        # _______________Tab 4__________________#
    
        base_frame_tab_4 = tk.Frame( my_notebook, width = 1280, height = 5000, bg = "#65A8E8" )
    
        # Adding scrollbar to that tab
        base_canvas_tab_4 = tk.Canvas( base_frame_tab_4, width = 1250, height = 5000 )
        base_canvas_tab_4.pack( side = tk.LEFT, fill = tk.BOTH, expand = 1 )
        my_scrollbar = ttk.Scrollbar( base_frame_tab_4, orient = tk.VERTICAL, command = base_canvas_tab_4.yview )
        my_scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        base_canvas_tab_4.configure( yscrollcommand = my_scrollbar.set )
        base_canvas_tab_4.bind( '<Configure>', lambda e : base_canvas_tab_4.configure( scrollregion = base_canvas_tab_4.bbox( "all" ) ) )
        tab_frame_4 = tk.Frame( base_canvas_tab_4, width = 1280, height = 5000, bg = "#65A8E8" )
        base_canvas_tab_4.create_window( (0, 0), window = tab_frame_4, anchor = "nw" )
    
        # ____Stuff in the tab___#
    
        bg_label_4 = tk.Label( tab_frame_4, text = 'Dislikes Vs Videos Downloaded', bg = '#65A8E8', font = ("Calibre", 30) )
        bg_label_4.place( relx = 0.3, rely = 0.01 )
        dislikes_graph_img = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/dislikes_bar_graph.png' ) )
        dislikes_graph_img_lbl = tk.Label( tab_frame_4, image = dislikes_graph_img )
        dislikes_graph_img_lbl.place( relx = 0.25, rely = 0.03 )
        dislikes_graph_img_2 = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/dislikes_hist_graph.png' ) )
        dislikes_graph_img_2_lbl = tk.Label( tab_frame_4, image = dislikes_graph_img_2 )
        dislikes_graph_img_2_lbl.place( relx = 0.25, rely = 0.13 )
    
        # ___#
    
        # _______________Tab 5__________________#
    
        base_frame_tab_5 = tk.Frame( my_notebook, width = 1280, height = 5000, bg = "#65A8E8" )
    
        # Adding scrollbar to that tab
        base_canvas_tab_5 = tk.Canvas( base_frame_tab_5, width = 1250, height = 5000 )
        base_canvas_tab_5.pack( side = tk.LEFT, fill = tk.BOTH, expand = 1 )
        my_scrollbar = ttk.Scrollbar( base_frame_tab_5, orient = tk.VERTICAL, command = base_canvas_tab_5.yview )
        my_scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        base_canvas_tab_5.configure( yscrollcommand = my_scrollbar.set )
        base_canvas_tab_5.bind( '<Configure>', lambda e : base_canvas_tab_5.configure( scrollregion = base_canvas_tab_5.bbox( "all" ) ) )
        tab_frame_5 = tk.Frame( base_canvas_tab_5, width = 1280, height = 5000, bg = "#65A8E8" )
        base_canvas_tab_5.create_window( (0, 0), window = tab_frame_5, anchor = "nw" )
    
        # ____Stuff in the tab___#
    
        bg_label_5 = tk.Label( tab_frame_5, text = 'Categories Vs Videos Downloaded', bg = '#65A8E8', font = ("Calibre", 30) )
        bg_label_5.place( relx = 0.3, rely = 0.01 )
        categories_graph_img = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/categories_bar_graph.png' ) )
        categories_graph_img_lbl = tk.Label( tab_frame_5, image = categories_graph_img )
        categories_graph_img_lbl.place( relx = 0.25, rely = 0.03 )
        categories_graph_img_2 = ImageTk.PhotoImage( Image.open( 'Assets/Graphs/categories_pie_chart.png' ) )
        categories_graph_img_2_lbl = tk.Label( tab_frame_5, image = categories_graph_img_2 )
        categories_graph_img_2_lbl.place( relx = 0.25, rely = 0.13 )
    
        # ___#
    
        # ____________End of declaring Tabs_____________#
        # ___________Adding them to the notebook, and activating them_________#
    
        base_frame_tab_1.pack( fill = "both", expand = 1 )
        base_frame_tab_2.pack( fill = "both", expand = 1 )
        base_frame_tab_3.pack( fill = "both", expand = 1 )
        base_frame_tab_4.pack( fill = "both", expand = 1 )
        base_frame_tab_5.pack( fill = "both", expand = 1 )
    
        my_notebook.add( base_frame_tab_1, text = "Views" )
        my_notebook.add( base_frame_tab_2, text = "Ratings" )
        my_notebook.add( base_frame_tab_3, text = "Likes" )
        my_notebook.add( base_frame_tab_4, text = "Dislikes" )
        my_notebook.add( base_frame_tab_5, text = "Categories" )
    
        root.mainloop()

class loading(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('445x245')
        BG_IMG = "Assets/Background Images/metadata_img.png"
        self.imgg = tk.PhotoImage( file = BG_IMG, master = self )
        self.label = tk.Label( self, image = self.imgg )
        self.label.place(relx = -0.01, rely = -0.01)
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=450 , mode="determinate", style="TProgressbar")
        self.progress.place(rely = 0.65, relx = -0.01, relheight = 0.08)
        self.bytes = 0
        self.maxbytes = 0
        self.start()
    
    def start(self):
        self.progress["value"] = 0
        self.maxbytes = int(1.5*len(playlist_URLS))
        self.progress["maximum"] = int(1.5*len(playlist_URLS))
        self.read_bytes()
    
    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 0.1
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)
            if done:
                self.destroy()
        else:
            while True:
                if done:
                    self.destroy()
                    break

def generate_vids() :
    global done, video_titles, video_titles_with_urls
    video_titles_with_urls = [[] for i in range(len(playlist_URLS))]
    print(video_titles_with_urls)
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
    with ydl:
        result = ydl.extract_info(URL,download=False)
        print('done')
        if 'entries' in result:
            video = result['entries']
            j = 0
            for i, item in enumerate(video):
                video_titles.append(result['entries'][i]['title'])
                video_titles_with_urls[j].append(video_titles[j])
                video_titles_with_urls[j].append(playlist_URLS[j])
                print(video_titles_with_urls)
                j = j+1
            fio.write.add_playlist_to_csv(video, len(playlist_URLS))
        done = True
        print(like_counts, dislike_counts)

# Function to run all the things. Function to return to. Function that calls. Function that manages.
def main() :
    global again, playlist_URLS
    while again :
        # Graphs.plot_ratings_vs_videos()
        # Graphs.plot_views_vs_videos()
        again = False
        window.intro_win()  # gets the URL
        if TYPE == 'SINGLE' :
            # youtube object used to getting info that is common to both single and playlist downlaods
            yt = pt.YouTube( URL )
            fio.write.add_to_data_csv( yt, URL )
            window.sel_download_win_single( URL, yt )
        elif TYPE == 'PLAYLIST' :
            playlist = pt.Playlist( URL )
            playlist._video_regex = re.compile( r"\"url\":\"(/watch\?v=[\w-]*)" )
            playlist_URLS = playlist.video_urls
            print(playlist_URLS[0])
            T1 = threading.Thread( target = generate_vids )
            T1.start()
            app = loading()
            T2 = threading.Thread( target = app.mainloop() )
            T2.start()
            window.sel_downlaod_win_playlist( playlist )
        elif TYPE == 'STATISTICS' :
            window.statistics()
    
    if not again :
        print( 'Thanks for using Kappa video downloader' )

main()