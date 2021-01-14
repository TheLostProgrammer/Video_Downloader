from tkinter import *
from pytube import YouTube, Playlist
import pafy
import glob
import os
import re
import requests
import platform
import earthpy as et
import urllib.request

# setting screen size and title of window
window = Tk()
window.geometry("380x350")
window.title("Youtube Video Downloader")

# input for URL location for a video
video_url_label = StringVar()
video_url_input = StringVar()
video_url_label.set("\nEnter the Youtube Video URL")
Label(window, textvariable=video_url_label).pack()
Entry(window, textvariable=video_url_input, width=30).pack()

# input for download location for a video
video_location_label = StringVar()
video_location_input = StringVar()
video_location_label.set("\nEnter download location")
Label(window, textvariable=video_location_label).pack()
Entry(window, textvariable=video_location_input, width=30).pack()

# check OS
if len(video_location_input.get()) == 0:
    video_location_input = et.io.HOME+"/Downloads"


# input for resolution for a video
video_resolution_label = StringVar()
video_resolution_input = StringVar()
video_resolution_label.set("\nEnter desired resolution (Make sure video supports it)\n1080p recommended and not above")
Label(window, textvariable=video_resolution_label).pack()
Entry(window, textvariable=video_resolution_input, width=30).pack()


def video():
    # # if not errors occur this code will be run
    # try:
    # checking if URL is a YouTube video URL
    if str(video_url_input.get()[0:30]) == "https://www.youtube.com/watch?":
        # removing special characters from video title
        result1 = ""
        result = pafy.new(video_url_input.get())
        for letter in result.title:
            if letter not in "~`!@#$%^&*()_+-={}[]|\\:;\"',./< >?":
                result1 += letter
        print(result1)
        name = result.title

        # changing the label widgets text
        video_url_label.set("Downloading...")
        video_location_label.set("Getting file location...")
        video_resolution_label.set("Getting desired resolution...")
        error1.set("")
        window.update()

        # getting resolution input for video
        if len(video_resolution_input.get()) > 0:
            YouTube(video_url_input.get()).streams.filter(res=video_resolution_input.get()).first().download(video_location_input.get(), filename="video_file8757")
        else:
            link = YouTube(video_url_input.get())
            result = []
            for i in link.streams:
                result.append(i.resolution)
            print(result)

            # checking if resolution is in the videos available resolutions
            if "1440p" in result or "1080p" in result:
                x = "1080p"
                YouTube(video_url_input.get()).streams.filter(res=x).first().download(video_location_input.get(), filename="video_file8757")
            else:
                YouTube(video_url_input.get()).streams.get_highest_resolution().download(video_location_input.get(), filename="video_file8757")
        YouTube(video_url_input.get()).streams.filter(only_audio=True).first().download(video_location_input.get(), filename="audio_file7574")

        # combining the files
        os.system(f"ffmpeg -i {video_location_input.get()}/video_file8757.mp4 -i {video_location_input.get()}/audio_file7574.mp4 -c:v copy -c:a aac {video_location_input.get()}/{result1}.mp4")

        # deleting the files
        for i in glob.glob("{}/video_file8757.mp4".format(video_location_input.get())):
            os.remove(i)
        for i in glob.glob("{}/audio_file7574.mp4".format(video_location_input.get())):
            os.remove(i)

        # renaming the result file to be the name you find it on YouTube
        os.rename(fr'{video_location_input.get()}/{result1 + ".mp4"}',
                  fr'{video_location_input.get()}/{name + ".mp4"}')

        # updating the labels
        video_url_label.set("Video Downloaded Successfully")
        video_location_label.set("Check your download location to find file")
        video_resolution_label.set(f"The resolution of the video is {video_resolution_input.get()}")

    # checking if URL is a YouTube Playlist URL
    elif str(video_url_input.get()[0:33]) == "https://www.youtube.com/playlist?":
        video_url_label.set("Downloading...")
        video_location_label.set("Getting file location...")
        video_resolution_label.set("Getting desired resolution...")
        error1.set("")
        window.update()

        # getting the URL and setting it as a playlist
        play_list = Playlist(video_url_input.get())
        print(len(play_list))

        # making sure that the folder name is correct and if not, renaming it
        folder_name = ""
        original_folder_name = ""
        for letter in video_location_input.get():
            original_folder_name += letter
            if letter not in " ":
                folder_name += letter
        new_folder_name = video_location_input.get().replace(original_folder_name, folder_name)
        os.rename(fr'{original_folder_name}',
                  fr'{new_folder_name}')

        # getting the link
        for video in play_list.videos:
            name = video.title
            result = []

            # getting resolution of the video and appending it to a list
            for i in video.streams:
                result.append(i.resolution)

            # checking if the user entered any input for resolution
            if len(video_resolution_input.get()) > 0:
                video.streams.filter(res=video_resolution_input.get()).first().download(new_folder_name, filename="video_file8757")
            else:
                # checking if the resolution is in the result list
                if "1440p" in result or "1080p" in result:
                    x = "1080p"
                    video.streams.filter(res=x).first().download(new_folder_name, filename="video_file8757")
                else:
                    video.streams.get_highest_resolution().download(new_folder_name, filename="video_file8757")
            video.streams.filter(only_audio=True).first().download(new_folder_name, filename="audio_file7574")

            # getting name of video (Removing all special characters)
            result1 = ""
            for letter in name:
                if letter not in "~`!@#$%^&*()_+-={}[]|\\:;\"',./< >?":
                    result1 += letter
            print(name)
            print(result1)
            print(result)

            # combining the video file with the audio file
            os.system(
                f"ffmpeg -i {new_folder_name}/video_file8757.mp4 -i {new_folder_name}/audio_file7574.mp4 -c:v copy -c:a aac {new_folder_name}/{result1}.mp4")

            # removing the original files
            for i in glob.glob(f"{new_folder_name}/video_file8757.mp4"):
                os.remove(i)
            for i in glob.glob(f"{new_folder_name}/audio_file7574.mp4"):
                os.remove(i)

            # renaming final file
            result_file_name = ""
            for letter in name:
                if letter in "\\/":
                    result_file_name += "|"
                else:
                    result_file_name += letter

            os.rename(fr'{new_folder_name}/{result1 + ".mp4"}',
                      fr'{new_folder_name}/{result_file_name + ".mp4"}')

            # changing GUI Labels
            video_url_label.set("Video Downloaded Successfully")
            video_location_label.set("Check your download location to find file")
            video_resolution_label.set(f"The resolution of the video is {video_resolution_input.get()}")
    elif str(video_url_input.get()[0:24]) == "https://www.facebook.com" and "videos" in str(video_url_input.get()):
        pass
    if mp3_mp4_input.get().lower() =="mp3":

    else:
        error1.set("Unknown Error has occurred.")

    # this code is run if an error occurs
    # except Exception as e:
    #     print(len(str(e)))
    #     if len(str(e)) > 50:
    #         s = str(e) + " " + "\nContact caleb.pierce1@outlook.com to resolve problem."
    #         error1.set("\n".join([s[i:i + 50] for i in range(0, len(s), 50)]))
    #     else:
    #         error1.set(f"Error:\n{str(e)}\n\ncontact caleb.pierce1@outlook.com to resolve problem")
    #     window.update()


# button for video function
Button(window, text="Download", command=video).pack()

# error reports placed on screen (for video function)
error1 = StringVar()
error1.set("")
Label(window, textvariable=error1).pack()


window.mainloop()
