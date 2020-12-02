"""
This file is used to define functions that are going to take in a youtube object, and then write the data onto files.
"""
# import pytube as pt


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
    
def get_data():
    video = pt.YouTube('https://www.youtube.com/watch?v=8kooIgKESYE')
    # video = pt.YouTube('https://www.youtube.com/watch?v=KRaWnd3LJfs')
    print(video.title)
    print(video.author)
    print(video.thumbnail_url)
    print(video.watch_url)
    print(video.age_restricted)
    print(video.rating)
    print(video.length)
    #print(video.streams)
    print(video.captions)
    print(video.description)
    print(video.caption_tracks)
    print(video.publish_date)
    print(video.views)

class write:
    @staticmethod
    def add_to_data(video):
        with open('data/Video titles.txt', 'a') as fout:
            with open( 'data/Video titles.txt', 'r' ) as fin :
                video_titles = fin.readlines()
            if video.title + '\n' not in video_titles:
                fout.write(video.title + '\n')
        length = conv_len(video.length)
        with open('data/Video lengths.txt', 'a') as fout:
            with open( 'data/Video lengths.txt', 'r' ) as fin :
                video_lengths = fin.readlines()
            if length + '\n' not in video_lengths:
                fout.write(length + '\n')
        with open('data/Video views.txt', 'a') as fout:
            with open( 'data/Video views.txt', 'r' ) as fin :
                video_views = fin.readlines()
                print(video_views)
            if video.views.__str__() + '\n' not in video_views:
                fout.write(video.views.__str__() + '\n')
        with open('data/Video authors.txt', 'a') as fout:
            with open( 'data/Video authors.txt', 'r' ) as fin :
                video_authors = fin.readlines()
            if video.author + '\n' not in video_authors:
                fout.write(video.author + '\n')
        with open('data/Video ratings.txt', 'a') as fout:
            with open( 'data/Video ratings.txt', 'r' ) as fin :
                video_ratings = fin.readlines()
            if video.rating.__str__() + '\n' not in video_ratings:
                fout.write(video.rating.__str__() + '\n')
        with open('data/Video publish_dates.txt', 'a') as fout:
            with open( 'data/Video publish_dates.txt', 'r' ) as fin :
                video_publish_dates = fin.readlines()
            if video.publish_date.__str__() + '\n' not in video_publish_dates:
                fout.write(video.publish_date.__str__() + '\n')
        with open('data/Video age_restriction.txt', 'a') as fout:
            with open( 'data/Video age_restriction.txt', 'r' ) as fin :
                video_ageRestricted_list = fin.readlines()
            if video.age_restricted.__str__() + '\n' not in video_ageRestricted_list:
                fout.write(video.age_restricted.__str__() + '\n')
        
class read:
    @staticmethod
    def get_title():
        with open('data/Video titles.txt', 'r') as fin:
            titles_list = fin.readlines()
            return titles_list
    @staticmethod
    def get_views():
        with open('data/Video views.txt', 'r') as fin:
            views_list = fin.readlines()
            return views_list
    @staticmethod
    def get_ratings():
        with open('data/Video ratings.txt', 'r') as fin:
            ratings_list = fin.readlines()
            return ratings_list
    @staticmethod
    def get_publish_dates():
        with open('data/Video publish_dates.txt', 'r') as fin:
            publish_dates_list = fin.readlines()
            return publish_dates_list
    @staticmethod
    def get_lengths():
        with open('data/Video lengths.txt', 'r') as fin:
            lengths_list = fin.readlines()
            return lengths_list
    @staticmethod
    def get_authors():
        with open('data/Video authors.txt', 'r') as fin:
            authors_list = fin.readlines()
            return authors_list
    @staticmethod
    def get_age_restriction():
        with open('data/Video age_restriction.txt', 'r') as fin:
            age_restriction_list = fin.readlines()
            return age_restriction_list