"""
This file is used to define functions that are going to take in a youtube object, and then write the data onto files.
"""
# import pytube as pt
import youtube_dl
ydl_opts = {}




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
        new_entry = True
        print('data writing')
        # getting likes and dislikes via youtube-dl
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
                    'https://www.youtube.com/watch?v=9bZkp7q19f0', download=False)
            video_likes = meta['like_count']
            video_dislikes = meta['dislike_count']
            video_category = meta['categories'][0]
            video_date = meta['upload_date']
        with open('data/Video titles.txt', 'a') as fout:
            with open( 'data/Video titles.txt', 'r' ) as fin :
                video_titles = fin.readlines()
            if video.title + '\n' not in video_titles:
                new_entry = True
                fout.write(video.title + '\n')
                length = conv_len(video.length)
            else: new_entry = False
            
        if new_entry:
            with open('data/Video lengths.txt', 'a') as fout:
                with open( 'data/Video lengths.txt', 'r' ) as fin :
                    fout.write(length + '\n')
            with open('data/Video views.txt', 'a') as fout:
                with open( 'data/Video views.txt', 'r' ) as fin :
                    fout.write(video.views.__str__() + '\n')
            with open('data/Video likes.txt', 'a') as fout:
                with open( 'data/Video likes.txt', 'r' ) as fin :
                    fout.write(video_likes.__str__() + '\n')
            with open('data/Video dislikes.txt', 'a') as fout:
                with open( 'data/Video dislikes.txt', 'r' ) as fin :
                    fout.write(video_dislikes.__str__() + '\n')
            with open('data/Video authors.txt', 'a') as fout:
                with open( 'data/Video authors.txt', 'r' ) as fin :
                    fout.write(video.author + '\n')
            with open('data/Video ratings.txt', 'a') as fout:
                with open( 'data/Video ratings.txt', 'r' ) as fin :
                    fout.write(video.rating.__str__() + '\n')
            with open('data/Video publish_dates.txt', 'a') as fout:
                with open( 'data/Video publish_dates.txt', 'r' ) as fin :
                    fout.write(video_date.__str__() + '\n')
            with open('data/Video categories.txt', 'a') as fout:
                with open( 'data/Video categories.txt', 'r' ) as fin :
                    fout.write(video_category.__str__() + '\n')
      
    @staticmethod
    def add_to_data_playlist(video):
        for i, item in enumerate(video):
            new_entry = True
            single_vid_title = video[i]['title']
            with open('data/Video titles.txt', 'a') as fout:
                with open( 'data/Video titles.txt', 'r' ) as fin :
                    video_titles = fin.readlines()
                if single_vid_title + '\n' not in video_titles:
                    new_entry = True
                    fout.write(single_vid_title + '\n')
                else: new_entry = False

            if new_entry:
                with open('data/Video lengths.txt', 'a') as fout:
                    with open( 'data/Video lengths.txt', 'r' ) as fin :
                        fout.write(conv_len(int(video[i]['duration'])) + '\n')
                with open('data/Video views.txt', 'a') as fout:
                    with open( 'data/Video views.txt', 'r' ) as fin :
                        fout.write(video[i]['view_count'].__str__() + '\n')
                with open('data/Video likes.txt', 'a') as fout:
                    with open( 'data/Video likes.txt', 'r' ) as fin :
                        fout.write(video[i]['like_count'].__str__() + '\n')
                with open('data/Video dislikes.txt', 'a') as fout:
                    with open( 'data/Video dislikes.txt', 'r' ) as fin :
                        fout.write(video[i]['dislike_count'].__str__() + '\n')
                with open('data/Video authors.txt', 'a') as fout:
                    with open( 'data/Video authors.txt', 'r' ) as fin :
                        fout.write(video[i]['uploader'] + '\n')
                with open('data/Video ratings.txt', 'a') as fout:
                    with open( 'data/Video ratings.txt', 'r' ) as fin :
                        fout.write(video[i]['average_rating'].__str__() + '\n')
                with open('data/Video publish_dates.txt', 'a') as fout:
                    with open( 'data/Video publish_dates.txt', 'r' ) as fin :
                        fout.write(video[i]['upload_date'].__str__() + '\n')
                with open('data/Video categories.txt', 'a') as fout:
                    with open( 'data/Video categories.txt', 'r' ) as fin :
                        fout.write(video[i]['categories'][0].__str__() + '\n')
                print('done lol')
        

class read:
    @staticmethod
    def get_titles():
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
    def get_categories():
        with open('data/Video categories.txt', 'r') as fin:
            video_category_list = fin.readlines()
            return video_category_list
    @staticmethod
    def get_likes():
        with open('data/Video likes.txt', 'r') as fin:
            video_likes_list = fin.readlines()
            return video_likes_list
    @staticmethod
    def get_dislikes():
        with open('data/Video dislikes.txt', 'r') as fin:
            video_dislikes_list = fin.readlines()
            return video_dislikes_list