import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import numpy as np
import os
import cv2
from threading import Thread

def audio_rec():                               # audio recorder function  

    fs = 44100 #frame rates
    sec = 12                # total seconds for recording audio

    myrecording = sd.rec(int(sec * fs), samplerate=fs, channels=2)
    sd.wait(1)
    write('output1.wav',fs,myrecording)

    

def video_rec():            #video recorder main function 
    filename = 'video.avi'
    frames_per_second = 24.0
    res = '720p'

    # Set resolution for the video capture
   
    def change_res(cap, width, height):
        cap.set(3, width)
        cap.set(4, height)

    # Standard Video Dimensions Sizes
    STD_DIMENSIONS =  {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }


    # grab resolution dimensions and set video capture to it.
    def get_dims(cap, res='1080p'):
        width, height = STD_DIMENSIONS["480p"]
        if res in STD_DIMENSIONS:
            width,height = STD_DIMENSIONS[res]
        ## change the current caputre device
        ## to the resulting resolution
        change_res(cap, width, height)
        return width, height

    # Video Encoding, might require additional installs
    VIDEO_TYPE = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        #'mp4': cv2.VideoWriter_fourcc(*'H264'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    def get_video_type(filename):
        filename, ext = os.path.splitext(filename)
        if ext in VIDEO_TYPE:
            return  VIDEO_TYPE[ext]
        return VIDEO_TYPE['avi']



    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

    while True:
        ret, frame = cap.read()
        out.write(frame)
        #uncomment this section to watch camera stream on screen
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    out.release()
    cv2.destroyAllWindows()

Thread(target=audio_rec).start()    #threading both audio and video recording function 
Thread(target=video_rec).start()
