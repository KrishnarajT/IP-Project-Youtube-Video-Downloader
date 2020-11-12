# IP Project - Youtube Video Downloader

IP project made by :
1. Krishnaraj Thadesar
2. Siddharth Jana
4. Gourav Sharma

It aims to let you downlaod youtube vidoes with ease.


## Features:
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

## Installation

### _To run the Program executable file_ (not added yet)
1. Windows  x86
2. Connection to the Internet

### _To compile and edit the source code in your own Environment_ *(for collaborators)* :

1. _Python 3.7 to 3.9_ as of date of upload
2. Modules _pytube 9.7_, _pillow_, _requests_, _pandas_, _matplotlib_

```shell script
pip install pytube
pip install pillow
pip install requests
pip install pandas
pip install matplotlib
```

### Using the existing Environment to compile, edit, and view Source code

1. **Pycharm, Thonny** or any text editor that supports addition of Virtual Environments
2. Download or clone the repository in your computer
3. Extract the zip file into a convenient folder
4. In Pycharm, Navigate to 
`Settings -> Interpreter Settings -> Change Interpreter -> add existing Interpreter -> navigate to '~/YtDownEnv/Scripts/python.exe'`
and select that as the interpreter
5. Run the code.


## Limitations
1. Can only download video+audio upto 720p
2. Maximum of 50 videos of a playlist can be downloaded at once
