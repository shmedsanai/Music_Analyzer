import tkinter as tk
import json
import os
import shutil
import os.path
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import math
import sys
import pydub
import numpy as np
import librosa, librosa.display
from pydub import AudioSegment
from moviepy.editor import *
from sklearn.model_selection import train_test_split
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tensorflow.python.keras.saving.hdf5_format import HDF5_OBJECT_HEADER_LIMIT
root = tk.Tk()
root.resizable(False, False)
root.title("Music Analyzer")
canvas = tk.Canvas(root, width=600,height=500, bg="black")
canvas.grid(columnspan=3,rowspan=7)

filename = ""
instructions6 = ""
def tab1():


 def tab2():
    def tab3():
        instructions2.destroy()
        instructions3.destroy()
        instructions4.destroy()
        instructions5.destroy()
        next_button.destroy()
        back_button.destroy()

        instructions6 = tk.Label(root, height=5 ,text="REGGAE is deeply linked to Rastafari, an Afrocentric religion which\n developed in Jamaica in the visibility The tempo of reggae is usually slower\n paced than both ska and rocksteady.", font="Raleway", bg="black",fg="white")
        instructions6.grid(column=1,row=0)
    
        instructions7 = tk.Label(root, height=5 ,text="BLUES is a music genre and musical form which was originated in the Deep\n South of the United States around the 1860s by African-Americans from roots", font="Raleway", bg="black",fg="white")
        instructions7.grid(column=1,row=1)

        instructions8 = tk.Label(root, height=5 ,text="DISCO is a genre of dance music and a subculture that emerged in the 1970s\n from the United States urban nightlife scene. Its sound is typified by\n four-on-the-floor beats, syncopated basslines, string sections", font="Raleway", bg="black",fg="white")
        instructions8.grid(column=1,row=2)

        instructions9 = tk.Label(root, height=5 ,text="HIPHOP is music and culture formed during the 1970s in New York City from the\n multicultural exchange between African-American \nwere of Latin American or Caribbean origin.", font="Raleway", bg="black",fg="white")
        instructions9.grid(column=1,row=3)

        def erase():
         instructions6.destroy()
         instructions7.destroy()
         instructions8.destroy()
         instructions9.destroy()
         home_button.destroy()
         back2_button.destroy()
         tab1()

        def erase3():
         instructions6.destroy()
         instructions7.destroy()
         instructions8.destroy()
         instructions9.destroy()
         home_button.destroy()
         back2_button.destroy()
         tab2()

        home_button = tk.Button(root,text='Home Page',command= erase,bg="#19941d",height=1,width=10, font="Raleway")
        home_button.grid(column=1,row=6)

        back2_button = tk.Button(root,text='Back',command= erase3,bg="#19941d",height=1,width=10, font="Raleway")
        back2_button.place(x=12,y=465)


        

    logo_label.destroy()
    instructions.destroy()
    open_button.destroy()
    anal_button.destroy()
    explore_button.destroy()

    instructions2 = tk.Label(root, height=5 ,text="JAZZ is a music genre which has been recognized as a major form of\n musical expression in traditional and popular music and is characterized by swing and\n blue notes", font="Raleway", bg="black",fg="white")
    instructions2.grid(column=1,row=0)
    
    instructions3 = tk.Label(root, height=5 ,text="METAL music revolves around a few key components: heavily distorted\n guitar riffs and chords, powerful drumming, extra low-range bass notes, and\n aggressive or throaty vocals.", font="Raleway", bg="black",fg="white")
    instructions3.grid(column=1,row=1)
    
    instructions4 = tk.Label(root, height=5 ,text="POP is a type of music, usually played on electronic instruments, thats\n popular with many people because it consists of short songs with a strong beat.", font="Raleway", bg="black",fg="white")
    instructions4.grid(column=1,row=2)
    
    instructions5 = tk.Label(root, height=5 ,text="ROCK is a music genre which has been recognized as a major form of\n musical expression in traditional and popular music and is characterized by swing and\n blue notes", font="Raleway", bg="black",fg="white")
    instructions5.grid(column=1,row=3)
    
    
    next_button = tk.Button(
    root,
    text='Next Page',
    command= tab3,
    bg="#19941d",height=1,width=10, font="Raleway"
    )

    next_button.grid(column=1,row=6)

    def erase2():
         instructions2.destroy()
         instructions3.destroy()
         instructions4.destroy()
         instructions5.destroy()
         back_button.destroy()
         next_button.destroy()
         tab1()

    back_button = tk.Button(
    root,
    text='Back',
    command= erase2,
    bg="#19941d",height=1,width=10, font="Raleway"
    )
   # back_button.place(x=12,y=449)
   #  back_button.grid(column=0,row=6)
    back_button.place(x=12,y=465)
    
    



 logo = Image.open('logo.PNG')
 logo = ImageTk.PhotoImage(logo)
 logo_label = tk.Label(image=logo, borderwidth=0)
 logo_label.image = logo
 logo_label.grid(column=1,row=0)

 instructions = tk.Label(root, text="Organize Your Music Library!", font="Raleway", bg="black",fg="white")
 instructions.grid(column=1,row=1)

# -------------------------------------------------------------------------------------------------------------


#  filepath = ""

 def select_file():
     filetypes = (
        ('.mp3 files', '*.mp3'),
        ('.mp4 files', '*.mp4'),
        ('.wav files', '*.wav'),
       
     )

     global filename
     filename = fd.askopenfilename(
        title='upload a file',
        initialdir='/',
        filetypes=filetypes)

     
     if(filename):
      showinfo(
        title='Selected File',
        message=os.path.basename(filename)
    )


 open_button = tk.Button(
     root,
     text='Open a File',
     command=select_file,
     bg="#19941d",height=2,width=15, font="Raleway"
)

 open_button.grid(column=1,row=2)

# -----------------------------------------------------------------
 
 def analyzation():
    current_directory = os.getcwd()
    print(current_directory)
    #global filename
    #use filename variable and attach code here
    if(filename):
     for fp in filename:
       ext = os.path.splitext(fp)[-1]
     print(ext)
     if ext == ".mp4":
       mp3_file="audio.mp3"
       videoclip=VideoFileClip(filename)
       audioclip=videoclip.audio
       audioclip.write_audiofile(mp3_file)
       audioclip.close()
       videoclip.close()
       #filename=mp3_file
     
     check=0
     ppath='C:\\Users\\Kayani\\source\\repos\\PythonApplication2\\PythonApplication2'
     fpath = os.path.normpath(filename)
     flname = os.path.basename(fpath)
     reconstructed_model = keras.models.load_model("Music_Genre_10_CNN.h5")
     index_genre = {0:"hiphop",1:"country",2:"jazz",3:"classical",4:"metal",5:"pop",6:"rock",7:"blues",8:"reggae",9:"disco"}

     
     
     song_mfcc = process_input(filename, 30)
    
     type(song_mfcc)
     X_predict = song_mfcc[np.newaxis, ..., np.newaxis]
     X_predict.shape
     X_predict = song_mfcc[np.newaxis, ..., np.newaxis]
     predict = reconstructed_model.predict(X_predict)
        # get index with max value
     predicted_index = np.argmax(predict, axis=1)
     print("Predicted Genre:", index_genre[int(predicted_index)])
     for root, dirs, files in os.walk(ppath):
         dpath = os.path.normpath(root)
         fname = os.path.basename(dpath)
         if fname == index_genre[int(predicted_index)]:
             check=1
             Lpath=dpath
     if check == 1:
         # check if file exist in destination
         if os.path.exists(Lpath + os.path.basename(filename)):
          # Split name and extension
          data = os.path.splitext(os.path.basename(filename))
          only_name = data[0]
          extension = data[1]
          # Adding the new name
          new_base = only_name + '_new' + extension
          # construct full file path
          new_name = os.path.join(Lpath, new_base)
          # move file
          shutil.move(filename , new_name)
         else:
          pp='\\'
          shutil.move(filename, Lpath + pp + os.path.basename(filename))   
     else:
         directory = index_genre[int(predicted_index)]
         # Parent Directory path
         parent_dir = ppath
         path = os.path.join(parent_dir, directory)
         os.mkdir(path)
         for root, dirs, files in os.walk(ppath):
          dpath = os.path.normpath(root)
          fname = os.path.basename(dpath)
          if fname == index_genre[int(predicted_index)]:
             check=1
             Lpath=dpath
     if check == 1:
         pp='\\'
         # check if file exist in destination
         if os.path.exists(Lpath + pp + os.path.basename(filename)):
          # Split name and extension
          data = os.path.splitext(os.path.basename(filename))
          only_name = data[0]
          extension = data[1]
          # Adding the new name
          new_base = only_name + '_new' + extension
          # construct full file path
          new_name = os.path.join(Lpath, new_base)
          # move file
          print(Lpath + pp + os.path.basename(filename))
          #shutil.move(filename , new_name)
         else:
          shutil.move(filename, Lpath + pp + os.path.basename(filename))
     showinfo(
        title='Success',
        message='Analyzation completed! Genre detected: '+ index_genre[int(predicted_index)]
    )
    else:
        showinfo(
        title='ERROR',
        message='Please select a file'
    )
 def process_input(audio_file, track_duration):

  SAMPLE_RATE = 22050
  NUM_MFCC = 13
  N_FTT=2048
  HOP_LENGTH=512
  TRACK_DURATION = track_duration # measured in seconds
  SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
  NUM_SEGMENTS = 10

  samples_per_segment = int(SAMPLES_PER_TRACK / NUM_SEGMENTS)
  

  signal, sample_rate = librosa.load(audio_file, sr=SAMPLE_RATE)
  
  for d in range(10):

    # calculate start and finish sample for current segment
    start = samples_per_segment * d
    finish = start + samples_per_segment

    # extract mfcc
    mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc=NUM_MFCC, n_fft=N_FTT, hop_length=HOP_LENGTH)
    mfcc = mfcc.T

    return mfcc


 anal_button = tk.Button(
    root,
    text='Analyze File',
    command= analyzation,
    bg="#19941d",height=2,width=15, font="Raleway"
    )

 anal_button.grid(column=1,row=3)

# -----------------------------------------------------------------------------


 explore_button = tk.Button(
    root,
    text='About Genre',
    command= tab2,
    bg="#19941d",height=2,width=15, font="Raleway"
    )

 explore_button.grid(column=1,row=6)

# -----------------------------------------------------------------------------


tab1()


root.mainloop()