#!/bin/python
from tkinter import *
from tkinter import filedialog
from pytube import YouTube, Playlist
import pafy
import glob
import os
import youtube_dl
from sys import platform
import ffmpeg
import sys
from os import path

# setting root window:
window = Tk()
window.title("Video Downloader")
# window.resizable(False, False)
window.geometry("450x350")

# setting switch state:
btnState = False


# setting switch function:
def switch():
    global btnState
    if platform == "linux" or platform == "linux2":
        btnState = None
        print("Linux System Theme")
        pass
    elif btnState:
        # Light Theme
        print("Light Theme")
        foreground_colour = "#000000"
        background_colour = "#FFFFFF"
        theme_button.config(text="Dark Theme", bg=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        url_label.config(background=background_colour, foreground=foreground_colour)
        url_input.config(background=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        location_label.config(background=background_colour, foreground=foreground_colour)
        location_input.config(background=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        browse_B.config(bg=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        resolution_label.config(background=background_colour, foreground=foreground_colour)
        resolution_entry.config(background=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        download_button.config(text="Download", bg=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        error.config(background=background_colour, foreground=foreground_colour)
        window.config(bg=background_colour)
        mp3_mp4.config(bg=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        btnState = False
    else:
        # Dark Theme
        print("Dark Theme")
        foreground_colour = "#FFFFFF"
        background_colour = "#1E1E1E"
        theme_button.config(text="Light Theme", bg=background_colour, foreground=background_colour, highlightbackground=background_colour)
        url_label.config(background=background_colour, foreground=foreground_colour)
        url_input.config(background=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        location_label.config(background=background_colour, foreground=foreground_colour)
        location_input.config(background=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        browse_B.config(bg=background_colour, foreground=background_colour, highlightbackground=background_colour)
        resolution_label.config(background=background_colour, foreground=foreground_colour)
        resolution_entry.config(background=background_colour, foreground=foreground_colour, highlightbackground=background_colour)
        download_button.config(text="Download", bg=background_colour, foreground=background_colour, highlightbackground=background_colour)
        window.config(bg=background_colour)
        error.config(background=background_colour, foreground=foreground_colour)
        mp3_mp4.config(bg=background_colour, foreground=background_colour, highlightbackground=background_colour)
        btnState = True


# setting switch state:
mp3_mp4_state = True


# setting switch function:
def mp3_mp4_switch():
    global mp3_mp4_state
    if mp3_mp4_state:
        mp3_mp4.config(text="MP3")
        print("MP3 Selected")
        mp3_mp4_state = False
    else:
        mp3_mp4.config(text="MP4")
        print("MP4 Selected")
        mp3_mp4_state = True


def browse():
    download_directory = filedialog.askdirectory(initialdir=location_input.get())
    if len(download_directory) > 0:
        location_input.delete(0, END)
        location_input.insert(0, download_directory)


# Night mode label:
url_label = Label(window, text="\nEnter URL of Youtube Video or Playlist")
url_label.grid(row=1, column=1)
url_input = Entry(window, text="1080p", width=30)
url_input.grid(row=2, column=1)

location_label = Label(window, text="\nChoose download location")
location_label.grid(row=3, column=1)
location_input = Entry(window, width=30)
location_input.grid(row=4, column=1)
location_input.insert(0, path.expanduser("~/Downloads"))

browse_B = Button(window, text="Browse", command=browse, width=10)
browse_B.grid(row=5, column=1)

resolution_label = Label(window, text="\nEnter desired resolution (Make sure video supports it)\n1080p recommended and not above")
resolution_label.grid(row=6, column=1)
resolution_entry = Entry(window, width=30)
resolution_entry.grid(row=7, column=1)
resolution_entry.insert(0, "1080p")

# theme widget
theme_button = Button(window, text="Dark Theme", borderwidth=0, command=switch, width=10)
theme_button.grid(row=2, column=0)
# theme widget
mp3_mp4 = Button(window, text="MP4", borderwidth=0, command=mp3_mp4_switch, width=10)
mp3_mp4.grid(row=3, column=0)


def downloader():
    if str(url_input.get()[0:30]) == "https://www.youtube.com/watch?" or str(url_input.get()[0:17]) == "https://youtu.be/":
        # removing special characters from video title
        print("Getting new file name")
        result1 = ""
        result = pafy.new(url_input.get())
        for letter in result.title:
            if letter not in "~`!@#$%^&*()_+-={}[]|\\:;\"',./< >?":
                result1 += letter
        print(result1)
        name = result.title

        # changing the label widgets text
        if mp3_mp4_state is True:
            url_label.config(text="\nDownloading...")
            location_label.config(text="\nGetting file location...")
            resolution_label.config(text="\nGetting desired resolution...")
            error.config(text="")
            window.update()

            # getting resolution input for video
            if len(resolution_entry.get()) > 0:
                print("Getting Resolutions...")
                link = YouTube(url_input.get())
                result = []
                for i in link.streams:
                    result.append(i.resolution)
                print(result)

            # checking if resolution is in the videos available resolutions
                if "2160p" in result or "1440p" in result or "1080p" in result:
                    x = "1080p"
                    print("Downloading Video...")
                    print("The resolution is going to be 1080p")
                    YouTube(url_input.get()).streams.filter(res=x).first().download(location_input.get(), filename="video_file8757")
                else:
                    print("Downloading Video...")
                    print(f"The resolution is going to be {link.streams.get_highest_resolution()}")
                    YouTube(url_input.get()).streams.get_highest_resolution().download(location_input.get(), filename="video_file8757")
            else:
                link = YouTube(url_input.get())
                result = []
                print("Getting resolutions...")
                for i in link.streams:
                    result.append(i.resolution)
                print(result)

                # checking if resolution is in the videos available resolutions
                if "2160p" in result or "1440p" in result or "1080p" in result:
                    x = "1080p"
                    print("Downloading Video...")
                    YouTube(url_input.get()).streams.filter(res=x).first().download(location_input.get(), filename="video_file8757")
                else:
                    print("Downloading Video...")
                    YouTube(url_input.get()).streams.get_highest_resolution().download(location_input.get(), filename="video_file8757")
            print("Downloading Audio...")
            YouTube(url_input.get()).streams.filter(only_audio=True).first().download(location_input.get(), filename="audio_file7574")

            # combining the files
            print("Combining Audio and Video")
            os.system(f"ffmpeg -i {location_input.get()}/video_file8757.mp4 -i {location_input.get()}/audio_file7574.mp4 -c:v copy -c:a aac {location_input.get()}/{result1}.mp4")

            # deleting the files
            print("Removing Files...")
            for i in glob.glob("{}/video_file8757.mp4".format(location_input.get())):
                os.remove(i)
            for i in glob.glob("{}/audio_file7574.mp4".format(location_input.get())):
                os.remove(i)

            # renaming the result file to be the name you find it on YouTube
            print("Renaming Final File...")
            os.rename(fr'{location_input.get()}/{result1 + ".mp4"}',
                      fr'{location_input.get()}/{name + ".mp4"}')

            # updating the labels
            url_label.config(text="\nVideo Downloaded Successfully")
            location_label.config(text="\nCheck your download location to find file")
            resolution_label.config(text=f"\nThe resolution of the video is {resolution_entry.get()}")
        else:
            print("Getting Ready....")
            url_label.config(text="\nDownloading...")
            location_label.config(text="\nGetting file location...")
            resolution_label.config(text="\nGetting desired resolution...")
            error.config(text="")
            print("Downloading Audio File...")
            YouTube(url_input.get()).streams.filter(only_audio=True).first().download(location_input.get(), filename="audio_file7574")
            print("Renaming File")
            os.rename(fr'{location_input.get()}/{"audio_file7574" + ".mp4"}', fr'{location_input.get()}/{name + ".mp3"}')

    elif str(url_input.get()[0:33]) == "https://www.youtube.com/playlist?":
        if mp3_mp4_state is True:
            url_label.config(text="\nDownloading...")
            location_input.config(text="\nGetting file location...")
            resolution_label.config(text="\nGetting desired resolution...")
            error.config(text="")
            window.update()

            # getting the URL and setting it as a playlist
            print("Getting URL ready...")
            play_list = Playlist(url_input.get())
            print(len(play_list))

            # making sure that the folder name is correct and if not, renaming it
            print("Fixing Folder Name...")
            folder_name = ""
            original_folder_name = ""
            for letter in location_input.get():
                original_folder_name += letter
                if letter not in " ":
                    folder_name += letter
            new_folder_name = location_input.get().replace(original_folder_name, folder_name)
            os.rename(fr'{original_folder_name}',
                      fr'{new_folder_name}')

            # getting the link
            print("Downloading each Video...")
            for video in play_list.videos:
                print("Downloading Video 1...")
                name = video.title
                result = []

                # getting resolution of the video and appending it to a list
                print("Getting Resolution...")
                for i in video.streams:
                    result.append(i.resolution)

                # checking if the user entered any input for resolution
                if len(resolution_entry.get()) > 0:
                    video.streams.filter(res=resolution_entry.get()).first().download(new_folder_name, filename="video_file8757")
                else:
                    # checking if the resolution is in the result list
                    if "1440p" in result or "1080p" in result:
                        x = "1080p"
                        print("Downloading Video File...")
                        video.streams.filter(res=x).first().download(new_folder_name, filename="video_file8757")
                    else:
                        print("Downloading Video File...")
                        video.streams.get_highest_resolution().download(new_folder_name, filename="video_file8757")
                print("Downloading Audio File...")
                video.streams.filter(only_audio=True).first().download(new_folder_name, filename="audio_file7574")

                # getting name of video (Removing all special characters)
                print("Getting New File...")
                result1 = ""
                for letter in name:
                    if letter not in "~`!@#$%^&*()_+-={}[]|\\:;\"',./< >?":
                        result1 += letter
                print(name)
                print(result1)
                print(result)

                # combining the video file with the audio file
                print("Combining Video and Audio...")
                os.system(
                    f"ffmpeg -i {new_folder_name}/video_file8757.mp4 -i {new_folder_name}/audio_file7574.mp4 -c:v copy -c:a aac {new_folder_name}/{result1}.mp4")

                # removing the original files
                print("Removing Files...")
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

                print("Renaming Final File...")
                os.rename(fr'{new_folder_name}/{result1 + ".mp4"}',
                          fr'{new_folder_name}/{result_file_name + ".mp4"}')

                # changing GUI Labels
                print("Done")
                url_label.config(text="\nVideo Downloaded Successfully")
                location_label.config(text="\nCheck your download location to find file")
                resolution_label.config(text=f"\nThe resolution of the video is {resolution_entry.get()}")
        else:
            url_label.config(text="\nDownloading...")
            location_input.config(text="\nGetting file location...")
            resolution_label.config(text="\nGetting desired resolution...")
            error.config(text="")
            window.update()
            play_list = Playlist(url_input.get())
            print(len(play_list))

            for video in play_list.videos:
                print("Getting Title")
                name = video.title
                video.streams.filter(only_audio=True).first().download(location_input.get(), filename="audio_file7574")
                result_file_name = ""
                print("Getting File Name")
                for letter in name:
                    if letter in "\\/":
                        result_file_name += "|"
                    else:
                        result_file_name += letter
                print("Renaming File")
                os.rename(fr'{location_input.get()}/{"audio_file7574" + ".mp4"}',
                          fr'{location_input.get()}/{result_file_name + ".mp3"}')



    else:
        print("Check if the URL is a valid Playlist or YouTube URL.")
        error.config(text="Check if the URL is a valid Playlist or YouTube URL.")

# button for video function
download_button = Button(window, text="Download", command=downloader, width=10)
download_button.grid(row=8, column=1)

# error reports placed on screen (for video function)
error = Label(window, text="")
error.grid(row=9, column=1)

# window in mainloop
window.mainloop()
