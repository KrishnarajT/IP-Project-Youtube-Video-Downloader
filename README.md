# IP Project - Youtube Video Downloader

IP project made by : _Group No. 5_
1. Krishnaraj Thadesar
2. Siddharth Jana
4. Gourav Sharma

# Aim
It aims to let you downlaod youtube vidoes, as well as youtube playlists with ease. You should also be able to see some graphs and statistics on the videos you downloaded. Ease of access and intuitive user experience.


# Features:
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
15. Makes use of OOP concepts like multitasking, parallel processing, modularity and polymorphism to work efficiently.


# Dependencies and System Requirements

1. Active Connection to internet while running the program
2. Minimum of a x64 or x86 computer
3. 100 MB RAM, 200 MB Free Storage Space
4. Monitor Resolution - 1280x720p 

# Installation

### _To run the Program executable file (You don't need Python installed to run)_

1. Click on `tags` on the right hand side of this page under `resources`
2. Go to the first pre release, and click to expand  `assets`
3. Download and run the installer `Kappa.V.1.2.exe` on your computer
4. Select destination folder to install the executable.
5. Run the `main.exe` file from the folder where you installed the program.

### _To compile and edit the source code in your own Environment_ *(for group)* :

1. _Python 3.7 to 3.9_ as of date of upload
2. Modules _pytube 9.7_, _pillow_, _requests_, _pandas_, _matplotlib_, _youtube-dl_

```shell script
pip install pytube
pip install pillow
pip install requests
pip install pandas
pip install matplotlib
pip install youtube-dl
```

### Using the existing Environment to compile, edit, and view Source code (for group)

1. **Pycharm, Thonny** or any text editor that supports addition of Virtual Environments
2. Download or clone the repository in your computer
3. Extract the zip file into a convenient folder
4. In Pycharm, Navigate to 
`Settings -> Interpreter Settings -> Change Interpreter -> add existing Interpreter -> navigate to '~/YtDownEnv/Scripts/python.exe'`
and select that as the interpreter
5. Run the code.


# Limitations and Scope
1. Can only download video+audio upto 720p
2. Some Playlist links aren't supported 
3. Only a maximum of 100 videos can be downlaod in a single playlist at once
4. Requires constant maintainance, and version updates.
5. Heavy Reliability on foreign Dependencies and modules.

# Working

### Pytube

Every youtube video has a URL that is unique to the video.

#### Single Video
Example : 
`https://www.youtube.com/watch?v=8kooIgKESYE`

This video has a common part `https://www.youtube.com/watch?v=` and a unique part
`8kooIgKESYE`

The string `8kooIgKESYE` is the identification for the video, and is the address
where the video is stored in the server. It is a base 64 number.

To uniquely store the thumbnails of the videos that we download in the project, we
use this number or string as the name of the thumbnail, as can be seen in the 
script.

Because not everyone has the same internet speed, when you upload a video, youtube
stores the video in many formats ranging from 144p to the highest resolution of the 
uploaded video

If the video is greater than 1080p in resolution, It is difficult for a 4G network
to download and render the video on the screens of the users, and hence it is 
broken into audio and video.

These different versions of the video, are called streams.

Pytube has a Youtube and a Playlist class. So to download a video, we create an
instance of the Class, an object, that has the urls of all these streams.

To download the video, the user selects the quality and we give that quality of stream
to pytube's youtube object, after which we can downlaod the video.

#### Playlists

`https://www.youtube.com/watch?v=-GhzpvvIXlM&list=PLS1QulWo1RIY6fmY_iTjEhCMsdtAjgbZM`

is an example playlist, and follows much of the same rules as the other URL. A playlist is just 
a bunch of video URL's that are given a name, an author and creation time.

This data (the name, video urls etc are stored on the server, and that location
is provided to us bt the playlist URL)

so with this URL, we can simply get the Youtube video urls, and then the process of 
creation of a youtube object is repeated and the video is downlaoded.

_______________________



### Graphs and Data Storage

from the Youtube object, you can get data about the youtube video such as
1. title
2. views
3. rating
4. author
5. discription
6. Date of Publication
7. Likes to dislikes ratio
8. Like count and dislike count
etc

so After downlaoding a video, this data is written to a single file, stored in `data/video_(attribute)*`
that can be verified manually.

This data is written such that it does not overlap, and there are no repeated entries
Storing this data in files is so that it can be retrieved later. If it was not for 
files, we would save this data on an SQL server.

We can retrieve the data from these files using the `fileIO.py` file. This file has a 
`read` class, that has functions like `get_title()` or `get_views()` etc. These 
functions can be used to get a list that has all the titles or the authors or the views
of all the vidoes that we downloaded. 

The first element of each file corresponds to the first video downloaded.

these lists can then be further used to create pandas series, dataframes, and then
create graphs. These functions will be written in the `graphs.py` file.

These graphs are then integrated in the `main.py` file that are then displayed as 
statistics in the program.



# How it looks like

## _Intro Page - Entering Video URL_
![](https://github.com/KrishnarajT/IP-Project-Youtube-Video-Downloader/blob/main/Progress%20Images/12-11-20/Progress%20Screenshots%20(3).png)

## _Showing Video Information_ 
_Users can click the **download** button to download_

![](https://github.com/KrishnarajT/IP-Project-Youtube-Video-Downloader/blob/main/Progress%20Images/12-11-20/Progress%20Screenshots%20(1).png)

## _Downloaded Video_

_Users can click on **One more** to download more videos_

![](https://github.com/KrishnarajT/IP-Project-Youtube-Video-Downloader/blob/main/Progress%20Images/12-11-20/Progress%20Screenshots.png)

## _Downloading a Playlist_
![](https://github.com/KrishnarajT/IP-Project-Youtube-Video-Downloader/blob/main/Progress%20Images/12-11-20/Progress%20Screenshots%20(2).png)

## Loading Screen for Playlist
![]()

## _Downloaded and removed videos from the Playlist_
![](https://github.com/KrishnarajT/IP-Project-Youtube-Video-Downloader/blob/main/Progress%20Images/12-11-20/Progress%20Screenshots%20(4).png)

# Bibliograpy and Credits
Thanks to Teachers, Parents, and Group members for their support and Guidance

Credits to https://youtube.com/Codemy for help on learning tkinter.
Other helpful websites:

1. https://www.stackoverflow.com
2. https://www.github.com

Credits to the developers of modules like Pytube and youtube_dl.

