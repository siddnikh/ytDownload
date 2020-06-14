from pytube import YouTube
from sys import argv, exit
import os
import re
import imageio

#ffmpeg needs to be downloaded for working of moviepy, hence -
imageio.plugins.ffmpeg.download()
import moviepy.editor as mp

'''
STEPS:
#1: Download the video track and audio track from YouTube using pytube (in case there is no progressive stream found)
#2: Convert the audio track from mp4 to mp3 using moviepy
#3: Merge the video and audio tracks using moviepy
#4: Delete the seperate audio and video tracks
'''

#check
if len(argv) < 3:
    print("Wrong usage.\nUsage: python main.py [link] [resolution: example - 360p]")
    exit()

link = argv[1]
res = argv[2]

#STEP 1:

#returns a StreamQuery Object that consists of all the streams for that very specific video
streams = YouTube(link)
video_name = streams.title + " " + res
#A boolean variable to use later to check if we need seperate audio and video tracks
seperate_tracks = False

#returns a Stream Object that matches the resolution provided by the user, and is progressive
#A progressive stream consists of both, audio and video tracks, in a single file
progressive_stream = streams.streams.get_by_resolution(res)

if not progressive_stream:
    seperate_tracks = True
    print("Status: No Progressive Stream Found.\nWill try downloading seperate Audio and Video Tracks")

else:
    print("Status: Progressive Stream Found.")

#if there is no progressive stream found
if seperate_tracks:
    video_streams = streams.streams.filter(file_extension = 'mp4', res = res, only_video = True)
    audio_streams = streams.streams.filter(only_audio = True, file_extension = 'mp4')
    
    if not video_streams:
        print("Resolution not available for this video.")
        exit()
    #choosing the first stream from the list of streams we got
    audio_stream = audio_streams.first()
    print("Your audio Stream: " + str(audio_stream))
    
    #choosing the first stream from the list of streams we got (there is usually a single stream only)
    video_stream = video_streams.first()
    print("Your video Stream: " + str(video_stream))
    
    #DOWNLOADING THE FILES:
    output_path = os.path.join(os.getcwd(), "files\\")
    
    #VIDEO FILE:
    #this path will be used later
    video_path = (video_stream.download(output_path = output_path, filename = "video"))
    print("Your pre-processed video file is saved at: " + video_path)
    
    #AUDIO FILE:
    #this path will be used later
    audio_path = (audio_stream.download(output_path = output_path, filename = "audio"))
    print("Your pre-processed audio file is saved at: " + audio_path)

else:
    print("Your Progressive Stream: " + str(progressive_stream))
    
    output_path = os.path.join(os.getcwd(), "Downloaded\\")
    final_path = progressive_stream.download(output_path = output_path)
    
    print("Your Downloaded File can be found at: " + final_path + "\n\nThank you for using this service :)\nMade by Siddharth Nikhil")
    
    #We exit the program as we will have no need of further processing the files in case we did get a progressive stream
    exit()

#STEP 2:
#Setting the output path for the mp3 file
mp3_path = os.path.join(output_path, os.path.splitext(audio_path)[0] + '.mp3')

#creating a clip (not a subclip)
clip = mp.AudioFileClip(audio_path)
clip.write_audiofile(mp3_path)

mp3_path = output_path + "audio.mp3"

print("Status: Audio File Produced, can be found at: " + mp3_path)

#STEP 3:
#taking the audio file
audio = mp.AudioFileClip(mp3_path)

#taking the video file
video = mp.VideoFileClip(video_path)

#setting our video's audio 
final = video.set_audio(audio)
final.write_videofile(output_path + video_name + ".mp4")

#STEP 4:
os.remove(audio_path)
os.remove(mp3_path)
os.remove(video_path)
print("Your video can now be found at: " + output_path +" as" + video_name +".mp4")