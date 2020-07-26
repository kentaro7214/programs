#%%
import random
import os
import numpy
from scipy.io import wavfile
import pyaudio
import wave
import sys
import fcntl
import time
import pandas as pd
import math
import threading
#%%　コードと度数と周波数の定義。key_frequencyにキーと周波数の辞書として格納
tone = ["Ab","A","A#","Bb","B","C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#"]
chord = ["M7","m7","7","m7b5"]
tone_deg = {"Ab":-1,"A":0,"A#":1,"Bb":1,"B":2,"C":-9,"C#":-8,"Db":-8,"D":-7,"D#":-6,"Eb":-6,"E":-5,"F":-4,"F#":-3,"Gb":-3,"G":-2,"G#":-1}
chord_deg = ["M7","m7","7","m7b5"]
key_frequency = {}
degree = -9 
for k,v in tone_deg.items():
    key_frequency[k] = 440*2**(int(v)/12)

#%%　正弦波を作成するコマンド
def sine(frequency, length, rate):
  length = int(length * rate)
  factor = float(frequency) * (math.pi * 2) / rate
  return np.sin(np.arange(length) * factor)

#%% 　平均律で各種コードを定義。ルートからの度数乗してる。←純正律の方がゆらぎの関係

def Mm7(frequency, length, rate):
  # 音源生成
  src = []
  src.append(sine(frequency,length,rate))
  src.append(sine(frequency * math.pow(2,(4/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(7/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(10/12.0)),length,rate))
  res = numpy.array([0] * len(src[0])) #ダミーの空配列
 
  #加算&クリッピング
  for s in src:
    res = res + s
  res *= 0.5
  
  return res

def play_7(stream, frequency, length=240/int(sys.argv[1]), rate=44100):
  chunks = []
  chunks.append(Mm7(frequency, length, rate))
  chunk = numpy.concatenate(chunks) * 0.25
  stream.write(chunk.astype(numpy.float32).tobytes())


def M7(frequency, length, rate):
  # 音源生成
  src = []
  src.append(sine(frequency,length,rate))
  src.append(sine(frequency * math.pow(2,(4/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(7/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(11/12.0)),length,rate))
  res = numpy.array([0] * len(src[0])) #ダミーの空配列
 
  #加算&クリッピング
  for s in src:
    res = res + s
  res *= 0.5
  
  return res

def play_M7(stream, frequency, length=240/int(sys.argv[1]), rate=44100):
  chunks = []
  chunks.append(M7(frequency, length, rate))
  chunk = numpy.concatenate(chunks) * 0.25
  stream.write(chunk.astype(numpy.float32).tobytes())

def m7(frequency, length, rate):
  # 音源生成
  src = []
  src.append(sine(frequency,length,rate))
  src.append(sine(frequency * math.pow(2,(3/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(7/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(10/12.0)),length,rate))
  res = numpy.array([0] * len(src[0])) #ダミーの空配列
 
  #加算&クリッピング
  for s in src:
    res = res + s
  res *= 0.5
  
  return res

def play_m7(stream, frequency, length=240/int(sys.argv[1]), rate=44100):
  chunks = []
  chunks.append(m7(frequency, length, rate))
  chunk = numpy.concatenate(chunks) * 0.25
  stream.write(chunk.astype(numpy.float32).tobytes())

def m7b5(frequency, length, rate):
  # 音源生成
  src = []
  src.append(sine(frequency,length,rate))
  src.append(sine(frequency * math.pow(2,(3/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(7/12.0)),length,rate))
  src.append(sine(frequency * math.pow(2,(9/12.0)),length,rate))
  res = numpy.array([0] * len(src[0])) #ダミーの空配列
 
  #加算&クリッピング
  for s in src:
    res = res + s
  res *= 0.5
  
  return res

def play_m7b5(stream, frequency, length=240/int(sys.argv[1]), rate=44100):
  chunks = []
  chunks.append(m7b5(frequency, length, rate))
  chunk = numpy.concatenate(chunks) * 0.25
  stream.write(chunk.astype(numpy.float32).tobytes())


#%%　コードならす関数。選ばれたコードの文字列一致で条件付け。

def play_chord(chord,key):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
    channels=1, rate=44100, output=1)
    if chord == "M7":
        play_M7(stream,frequency=key_frequency[key])
        #print(key_frequency[key])
        #print("M7")
    if chord == "7":
        play_7(stream,frequency=key_frequency[key])
        #print(key_frequency[key])
        #print("7")
    if chord == "m7":
        play_m7(stream,frequency=key_frequency[key])
        #print(key_frequency[key])
        #print("m7")
    if chord == "m7b5":
        play_m7b5(stream,frequency=key_frequency[key])
        #print(key_frequency[key])
        #print("m7b5")
    stream.close()
    p.terminate()
def metro(BPM):
    os.system("afplay /System/Library/Sounds/Tink.aiff")
    time.sleep(60/BPM)
    os.system("afplay /System/Library/Sounds/Pop.aiff")
    time.sleep(60/BPM)
    os.system("afplay /System/Library/Sounds/Pop.aiff")
    time.sleep(60/BPM)
    os.system("afplay /System/Library/Sounds/Pop.aiff")
    time.sleep(60/BPM)
#%%
#sys.argv[2] = 2
count = 1
while count <= int(sys.argv[2]):
    print("loop" + str(count) + ":  3. 2. 1." )

    k1 = random.choice(tone)
    c1 = random.choice(chord)
    k2 = random.choice(tone)
    c2 = random.choice(chord)
    k3 = random.choice(tone)
    c3 = random.choice(chord)
    k4 = random.choice(tone)
    c4 = random.choice(chord)
    C1 = k1 + c1
    C2 = k2 + c2
    C3 = k3 + c3
    C4 = k4 + c4
    print(C1.ljust(16," ")+C2.ljust(16," ")+C3.ljust(16," ")+C4.ljust(16," "))
    metro(BPM=int(sys.argv[1]))
    print(" |")
    #metro(BPM=int(sys.argv[1]))
    play_chord(chord=c1,key=k1)
    print("                 |") 
    #metro(BPM=int(sys.argv[1]))
    play_chord(chord=c2,key=k2)
    print("                                 |")
    #metro(BPM=int(sys.argv[1]))
    play_chord(chord=c3,key=k3)
    print("                                                 |")
    #metro(BPM=int(sys.argv[1]))
    play_chord(chord=c4,key=k4)
    count +=1
    time.sleep(60/int(sys.argv[1]))
print("Finish")
os.system("afplay /System/Library/Sounds/Bottle.aiff")
