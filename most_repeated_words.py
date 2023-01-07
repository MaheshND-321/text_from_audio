# video to Audio conversion
###################################################
import os
import imageio
import moviepy.editor
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import speech_recognition as sr

Tk().withdraw()
filelocation = askopenfilename()

print('Conversion in progress...')

basename = os.path.basename(filelocation)

filename = os.path.splitext(basename)[0]

video = moviepy.editor.VideoFileClip(filelocation)
audio = video.audio

audio.write_audiofile(filename+".wav")
# print(aud)

print('Conversion Done Successfully!')

# Audio to text conversion
######################################################################
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
with sr.AudioFile('handsome.wav') as source:
    audio_text = r.listen(source)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')


# printing the frequently occuring words in the text
#################################################################
# Python program to find the k most frequent words
# from data set
from collections import Counter

data_set = text

# split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(6)

print("The Most Frequently occuring words in the video is : ",most_occur)
