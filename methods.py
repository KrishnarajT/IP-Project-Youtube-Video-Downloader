"""
This file has all the general methods that are used here and there in the window program
"""


import urllib.request
import os


# gets the id of the video from the url, this id is used to store the thumbnail of the video later on
def get_vid_id( url ) :
    return url[ url.index( "=" ) + 1 : ]

# Gets the video thumbnail and saves it in the correct folder
def get_video_tnl( url, tnurl ) :
    vid_id = get_vid_id( url ) + '.png'
    tnl = urllib.request.urlretrieve( tnurl, os.path.join( 'Assets/Thumbnails', vid_id ) )
    return tnl

# Convers the lengths of the videos from seconds to displayable and understandable formats
def conv_len( length ) :
    print( length )
    minutes_or_hours = length // 60  # 563
    if minutes_or_hours < 60 :
        print( minutes_or_hours )
        minutes = minutes_or_hours
        seconds = length - (60 * minutes)
        if minutes < 10 :
            vid_len = '00:0' + str( minutes ) + ':' + str( seconds )
        else :
            vid_len = '00:0' + str( minutes ) + ':' + str( seconds )
        return vid_len
    else :
        print( minutes_or_hours )
        hours = minutes_or_hours // 60
        print( 'hours', hours )
        minutes = (minutes_or_hours - (60 * hours))
        our_seconds = hours * 3600 + minutes * 60
        seconds = length - our_seconds
        if minutes < 10 and seconds < 10 :
            vid_len = str( hours ) + ':0' + str( minutes ) + ':0' + str( seconds )
        elif minutes < 10 and seconds > 10 :
            vid_len = str( hours ) + ':0' + str( minutes ) + ':' + str( seconds )
        else :
            vid_len = str( hours ) + ':' + str( minutes ) + ':' + str( seconds )
        
        return vid_len
