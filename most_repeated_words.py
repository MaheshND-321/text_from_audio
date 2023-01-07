# Video to Audio Convertion
##################################################################
# Author : Arnab Basak

import os
import imageio
import moviepy.editor
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filelocation = askopenfilename()

print('Conversion in progress...')

basename = os.path.basename(filelocation)

filename = os.path.splitext(basename)[0]

video = moviepy.editor.VideoFileClip(filelocation)
audio = video.audio

aud = audio.write_audiofile(filename+".wav")
print(aud)

print('Conversion Done Successfully!')


# Audio to text convertion
########################################################################
#import library
import speech_recognition as sr
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
with sr.AudioFile('short.wav') as source:
    audio_text = r.listen(source)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')


# printing most repitative words in the text
####################################################################################
text = 'Ramanujan spoke about black holes nearly 100 years or more than hundred years ago there was no concept of black mathematics for black holes when there was no concept of Black Hole science always progress is like this but the concept then the theory and then the mathematics but he made the mathematics first before before their eyes when they are and still more in our mathematics notebooks and netbooks mathematics sim ki foreigner my baby please mathematics'
count=0
maxcount = 0
l=[]
words = words=text.split()
for i in range(len(words)):
    for j in range(len(words)):
        if(words[i]==words[j]):        #finding count of each word
            count+=1
        else:
            count=count
        if(count==maxcount):          #comparing with maximum count
            l.append(words[i])
        elif(count>maxcount):         #if count greater than maxcount
            l.clear()
            l.append(words[i])
            maxcount=count
        else:
            l=l
        count=0
print(l)                              #printing contents of l
