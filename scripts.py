
import pydub
import glob
import os
from pydub import AudioSegment
import json
import audiosegment
from tqdm import tqdm
from pathlib import Path
import pandas as pd
music_path = '/home/hawau.toyin/Documents/data'

'''To change sample rate'''

def change_sr(filename, sr=44100):
    sound = AudioSegment.from_file(filename).set_frame_rate(sr)
    sound.export(filename)

undone =[]
for file in glob.iglob(music_path + '/*.mp3'):
    try:
        print('\n Changing sample rate for', file)
        change_sr(file)
    except Exception:
        undone.append(file)
        print('Unable to change', file)

'''To change file extension'''

undone =[]
def change_fileext(filename, ext='wav'):
    sound = AudioSegment.from_mp3(filename)
    filename = filename + '.wav'
    sound.export(filename, format='wav')


songs = list(glob.iglob('/home/metaverse/Documents/All_drums/*.mp3'))
for file in tqdm(songs):
    try:
        print('\n Changing extension for', file)
        change_fileext(file)
        os.remove(file)
    except Exception:
        undone.append(file)
        print('Unable to change', Exception)
print(undone)
    
'''Move by artist'''
for file in glob.iglob('/home/hawau.toyin/Documents/data-1/Moh*.wav'):
    os.rename(file, file.replace('data-1','Moh'))


'''Remove all mp3'''
songs = list(glob.iglob('/home/metaverse/Documents/asalah/*.mp3'))
for file in tqdm(songs):
    # print(os.path.basename(file)+'.mp3.wav')
    # print('Removing',file)
    os.remove(file)


