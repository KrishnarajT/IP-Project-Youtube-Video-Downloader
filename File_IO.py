"""
This file is used to define functions that are going to take in a youtube object, and then write the data onto files.
"""
# import pytube as pt
import youtube_dl, pandas as pd, numpy as np


ydl_opts = {}


def conv_len(length):
    minutes_or_hours = length // 60  # 563
    if minutes_or_hours < 60:
        minutes = minutes_or_hours
        seconds = length - (60 * minutes)
        if minutes < 10:
            vid_len = "00:0" + str(minutes) + ":" + str(seconds)
        else:
            vid_len = "00:0" + str(minutes) + ":" + str(seconds)
        return vid_len
    else:
        hours = minutes_or_hours // 60
        minutes = minutes_or_hours - (60 * hours)
        our_seconds = hours * 3600 + minutes * 60
        seconds = length - our_seconds
        if minutes < 10 and seconds < 10:
            vid_len = str(hours) + ":0" + str(minutes) + ":0" + str(seconds)
        elif minutes < 10 and seconds > 10:
            vid_len = str(hours) + ":0" + str(minutes) + ":" + str(seconds)
        else:
            vid_len = str(hours) + ":" + str(minutes) + ":" + str(seconds)

        return vid_len


class write:
    @staticmethod
    def add_to_data(video, url):
        # getting likes and dislikes via youtube-dl
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            video_likes = meta["like_count"]
            video_dislikes = meta["dislike_count"]
            video_category = meta["categories"][0]
            video_date = meta["upload_date"]
        with open("data/Video titles.txt", "a") as fout:
            with open("data/Video titles.txt", "r") as fin:
                video_titles = fin.readlines()
            if video.title + "\n" not in video_titles:
                new_entry = True
                fout.write(video.title + "\n")
                length = conv_len(video.length)
            else:
                new_entry = False

        if new_entry:
            with open("data/Video lengths.txt", "a") as fout:
                with open("data/Video lengths.txt", "r") as fin:
                    fout.write(length + "\n")
            with open("data/Video views.txt", "a") as fout:
                with open("data/Video views.txt", "r") as fin:
                    fout.write(video.views.__str__() + "\n")
            with open("data/Video likes.txt", "a") as fout:
                with open("data/Video likes.txt", "r") as fin:
                    fout.write(video_likes.__str__() + "\n")
            with open("data/Video dislikes.txt", "a") as fout:
                with open("data/Video dislikes.txt", "r") as fin:
                    fout.write(video_dislikes.__str__() + "\n")
            with open("data/Video authors.txt", "a") as fout:
                with open("data/Video authors.txt", "r") as fin:
                    fout.write(video.author + "\n")
            with open("data/Video ratings.txt", "a") as fout:
                with open("data/Video ratings.txt", "r") as fin:
                    fout.write(video.rating.__str__() + "\n")
            with open("data/Video publish_dates.txt", "a") as fout:
                with open("data/Video publish_dates.txt", "r") as fin:
                    fout.write(video_date.__str__() + "\n")
            with open("data/Video categories.txt", "a") as fout:
                with open("data/Video categories.txt", "r") as fin:
                    fout.write(video_category.__str__() + "\n")

    @staticmethod
    def add_to_data_playlist(video):
        for i, item in enumerate(video):
            new_entry = True
            single_vid_title = video[i]["title"]
            with open("data/Video titles.txt", "a") as fout:
                with open("data/Video titles.txt", "r") as fin:
                    video_titles = fin.readlines()
                if single_vid_title + "\n" not in video_titles:
                    new_entry = True
                    fout.write(single_vid_title + "\n")
                else:
                    new_entry = False

            if new_entry:
                with open("data/Video lengths.txt", "a") as fout:
                    with open("data/Video lengths.txt", "r") as fin:
                        fout.write(conv_len(int(video[i]["duration"])) + "\n")
                with open("data/Video views.txt", "a") as fout:
                    with open("data/Video views.txt", "r") as fin:
                        fout.write(video[i]["view_count"].__str__() + "\n")
                with open("data/Video likes.txt", "a") as fout:
                    with open("data/Video likes.txt", "r") as fin:
                        fout.write(video[i]["like_count"].__str__() + "\n")
                with open("data/Video dislikes.txt", "a") as fout:
                    with open("data/Video dislikes.txt", "r") as fin:
                        fout.write(video[i]["dislike_count"].__str__() + "\n")
                with open("data/Video authors.txt", "a") as fout:
                    with open("data/Video authors.txt", "r") as fin:
                        fout.write(video[i]["uploader"] + "\n")
                with open("data/Video ratings.txt", "a") as fout:
                    with open("data/Video ratings.txt", "r") as fin:
                        fout.write(video[i]["average_rating"].__str__() + "\n")
                with open("data/Video publish_dates.txt", "a") as fout:
                    with open("data/Video publish_dates.txt", "r") as fin:
                        fout.write(video[i]["upload_date"].__str__() + "\n")
                with open("data/Video categories.txt", "a") as fout:
                    with open("data/Video categories.txt", "r") as fin:
                        fout.write(video[i]["categories"][0].__str__() + "\n")

    @staticmethod
    def add_to_data_csv(video, url):

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            video_likes = meta["like_count"]
            video_dislikes = meta["dislike_count"]
            video_category = meta["categories"][0]
            video_date = meta["upload_date"]
        new_entry = True

        initial = read.get_df_from_csv()
        titles = initial["video_title"]
        for i in range(len(titles)):
            if video.title == titles[i]:
                new_entry = False
                break

        if new_entry:
            data = {
                "video_title": pd.Series([video.title], index=[0]),
                "video_views": pd.Series([video.views], index=[0]),
                "video_dislikes": pd.Series([video_dislikes], index=[0]),
                "video_likes": pd.Series([video_likes], index=[0]),
                "video_rating": pd.Series([video.rating], index=[0]),
                "video_length": pd.Series([conv_len(video.length)], index=[0]),
                "video_category": pd.Series([video_category], index=[0]),
                "video_author": pd.Series([video.author], index=[0]),
                "video_publish_date": pd.Series([video_date], index=[0]),
            }
            df = pd.DataFrame(data)
            df = pd.concat([initial, df], ignore_index=True)
            df.to_csv("Data/video_data.csv", index=False)

    @staticmethod
    def add_playlist_to_csv(video, number):
        video_titles = []
        video_ratings = []
        video_categories = []
        video_publish_dates = []
        video_authors = []
        video_likes = []
        video_dislikes = []
        video_views = []
        video_lengths = []

        initial = read.get_df_from_csv()
        for i, item in enumerate(video):
            new_entry = True
            single_vid_title = video[i]["title"]
            titles = initial["video_title"]
            # Check if the video already exists.
            for j in range(len(titles)):
                if single_vid_title == titles[j]:
                    return

            video_titles.append(video[i]["title"])
            video_ratings.append(video[i]["average_rating"])
            video_categories.append(video[i]["categories"])
            video_publish_dates.append(video[i]["upload_date"])
            video_authors.append(video[i]["uploader"])
            video_likes.append(video[i]["like_count"])
            video_dislikes.append(video[i]["dislike_count"])
            video_views.append(video[i]["view_count"])
            video_lengths.append(conv_len(int(video[i]["duration"])))

        data = {
            "video_title": pd.Series(video_titles),
            "video_views": pd.Series(video_views),
            "video_dislikes": pd.Series(video_dislikes),
            "video_likes": pd.Series(video_likes),
            "video_rating": pd.Series(video_ratings),
            "video_length": pd.Series(video_lengths),
            "video_category": pd.Series(video_categories),
            "video_author": pd.Series(video_authors),
            "video_publish_date": pd.Series(video_publish_dates),
        }
        df = pd.DataFrame(data)
        df = pd.concat([initial, df], ignore_index=True)
        df.to_csv("Data/video_data.csv", index=False)


class read:
    @staticmethod
    def get_titles():
        df = read.get_df_from_csv()
        return df["video_title"].tolist()

    @staticmethod
    def get_views():
        df = read.get_df_from_csv()
        return df["video_views"].tolist()

    @staticmethod
    def get_ratings():
        df = read.get_df_from_csv()
        return df["video_rating"].tolist()

    @staticmethod
    def get_publish_dates():
        df = read.get_df_from_csv()
        return df["video_publish_date"].tolist()

    @staticmethod
    def get_lengths():
        df = read.get_df_from_csv()
        return df["video_length"].tolist()

    @staticmethod
    def get_authors():
        df = read.get_df_from_csv()
        return df["video_author"].tolist()

    @staticmethod
    def get_categories():
        df = read.get_df_from_csv()
        return df["video_category"].tolist()

    @staticmethod
    def get_likes():
        df = read.get_df_from_csv()
        return df["video_likes"].tolist()

    @staticmethod
    def get_dislikes():
        df = read.get_df_from_csv()
        return df["video_dislikes"].tolist()

    @staticmethod
    def get_df_from_csv():
        return pd.read_csv("Data/video_data.csv")
