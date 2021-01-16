from tkinter import *
from tkinter import filedialog
from pytube import YouTube, Playlist
import pafy
import glob
import os
import youtube_dl
from os import path

try:
    # setting root window:
    window = Tk()
    window.title("Video Downloader")
    window.resizable(False, False)
    foreground_colour = "#000000"
    background_colour = "#FFFFFF"
    window.config(bg=background_colour)
    window.geometry("450x350")

    # setting switch state:
    btnState = False


    # setting switch function:
    def switch():
        global btnState
        if btnState:
            # Light Theme
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
            foreground_colour = "#FFFFFF"
            background_colour = "#000000"
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
        location_input.delete(0, END)
        location_input.insert(0, download_directory)


    # Night mode label:
    url_label = Label(window, text="\nEnter URL of Youtube Video or Playlist", foreground=foreground_colour, background=background_colour)
    url_label.place(x=105, y=0)
    url_input = Entry(window, text="1080p", width=30)
    url_input.place(x=90, y=40)

    location_label = Label(window, text="\nChoose download location")
    location_label.place(x=145, y=68)
    location_input = Entry(window, width=30)
    location_input.place(x=90, y=108)
    location_input.insert(0, path.expanduser("~/Downloads"))

    browse_B = Button(window, text="Browse", command=browse, width=10)
    browse_B.place(x=185, y=138)

    resolution_label = Label(window, text="\nEnter desired resolution (Make sure video supports it)\n1080p recommended and not above")
    resolution_label.place(x=65, y=165)
    resolution_entry = Entry(window, width=30)
    resolution_entry.place(x=90, y=220)
    resolution_entry.insert(0, "1080p")

    # theme widget
    theme_button = Button(window, text="Dark Theme", borderwidth=0, command=switch, highlightbackground=background_colour)
    theme_button.place(x=0, y=17)

    # theme widget
    mp3_mp4 = Button(window, text="MP4", borderwidth=0, command=mp3_mp4_switch, highlightbackground=background_colour)
    mp3_mp4.place(x=0, y=45)


    def downloader():
        try:
            if str(url_input.get()[0:30]) == "https://www.youtube.com/watch?" or str(url_input.get()[0:17]) == "https://youtu.be/":
                # removing special characters from video title
                result1 = ""
                result = pafy.new(url_input.get())
                for letter in result.title:
                    if letter not in "~`!@#$%^&*()_+-={}[]|\\:;\"',./< >?":
                        result1 += letter
                print(result1)
                name = result.title

                # changing the label widgets text
                if mp3_mp4_state is True:
                    url_label.config(text="Downloading...")
                    location_label.config(text="Getting file location...")
                    resolution_label.config(text="Getting desired resolution...")
                    error.config(text="")
                    window.update()

                    # getting resolution input for video
                    if len(resolution_entry.get()) > 0:
                        link = YouTube(url_input.get())
                        result = []
                        for i in link.streams:
                            result.append(i.resolution)
                        print(result)

                    # checking if resolution is in the videos available resolutions
                        if "2160p" in result or "1440p" in result or "1080p" in result:
                            x = "1080p"
                            YouTube(url_input.get()).streams.filter(res=x).first().download(location_input.get(), filename="video_file8757")
                        else:
                            YouTube(url_input.get()).streams.get_highest_resolution().download(location_input.get(), filename="video_file8757")
                    else:
                        link = YouTube(url_input.get())
                        result = []
                        for i in link.streams:
                            result.append(i.resolution)
                        print(result)

                        # checking if resolution is in the videos available resolutions
                        if "2160p" in result or "1440p" in result or "1080p" in result:
                            x = "1080p"
                            YouTube(url_input.get()).streams.filter(res=x).first().download(location_input.get(), filename="video_file8757")
                        else:
                            YouTube(url_input.get()).streams.get_highest_resolution().download(location_input.get(), filename="video_file8757")
                    YouTube(url_input.get()).streams.filter(only_audio=True).first().download(location_input.get(), filename="audio_file7574")

                    # combining the files
                    os.system(f"ffmpeg -i {location_input.get()}/video_file8757.mp4 -i {location_input.get()}/audio_file7574.mp4 -c:v copy -c:a aac {location_input.get()}/{result1}.mp4")

                    # deleting the files
                    for i in glob.glob("{}/video_file8757.mp4".format(location_input.get())):
                        os.remove(i)
                    for i in glob.glob("{}/audio_file7574.mp4".format(location_input.get())):
                        os.remove(i)

                    # renaming the result file to be the name you find it on YouTube
                    os.rename(fr'{location_input.get()}/{result1 + ".mp4"}',
                              fr'{location_input.get()}/{name + ".mp4"}')

                    # updating the labels
                    url_label.config(text="Video Downloaded Successfully")
                    location_label.config(text="Check your download location to find file")
                    resolution_label.config(text=f"The resolution of the video is {resolution_entry.get()}")
                else:
                    url_label.config(text="Downloading...")
                    location_label.config(text="Getting file location...")
                    resolution_label.config(text="Getting desired resolution...")
                    error.config(text="")
                    YouTube(url_input.get()).streams.filter(only_audio=True).first().download(location_input.get(), filename="audio_file7574")
                    os.rename(fr'{location_input.get()}/{"audio_file7574" + ".mp4"}', fr'{location_input.get()}/{name + ".mp3"}')

            elif str(url_input.get()[0:33]) == "https://www.youtube.com/playlist?":
                if mp3_mp4_state is True:
                    url_label.config(text="Downloading...")
                    location_input.config(text="Getting file location...")
                    resolution_label.config(text="Getting desired resolution...")
                    error.config(text="")
                    window.update()

                    # getting the URL and setting it as a playlist
                    play_list = Playlist(url_input.get())
                    print(len(play_list))

                    # making sure that the folder name is correct and if not, renaming it
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
                    for video in play_list.videos:
                        name = video.title
                        result = []

                        # getting resolution of the video and appending it to a list
                        for i in video.streams:
                            result.append(i.resolution)

                        # checking if the user entered any input for resolution
                        if len(resolution_entry.get()) > 0:
                            video.streams.filter(res=resolution_entry.get()).first().download(new_folder_name, filename="video_file8757")
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
                        url_label.config(text="Video Downloaded Successfully")
                        location_label.config(text="Check your download location to find file")
                        resolution_label.config(text=f"The resolution of the video is {resolution_entry.get()}")
                else:
                    url_label.config(text="Downloading...")
                    location_input.config(text="Getting file location...")
                    resolution_label.config(text="Getting desired resolution...")
                    error.config(text="")
                    window.update()
                    play_list = Playlist(url_input.get())
                    print(len(play_list))

                    for video in play_list.videos:
                        name = video.title
                        video.streams.filter(only_audio=True).first().download(location_input.get(), filename="audio_file7574")
                        result_file_name = ""
                        for letter in name:
                            if letter in "\\/":
                                result_file_name += "|"
                            else:
                                result_file_name += letter

                        os.rename(fr'{location_input.get()}/{"audio_file7574" + ".mp4"}',
                                  fr'{location_input.get()}/{result_file_name + ".mp3"}')



            else:
                error.config(text="Check if the URL is a valid Playlist or YouTube URL.")
        except Exception as e:
            print(e)
            error.config(text=e)

    # button for video function
    download_button = Button(window, text="Download", command=downloader, width=10)
    download_button.place(x=185, y=250)

    # error reports placed on screen (for video function)
    error = Label(window, text="")
    error.place(x=65, y=280)

    # window in mainloop
    window.mainloop()
except Exception as e:
    print(e)
    error.config(text=e)
