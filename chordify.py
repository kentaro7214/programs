#%%
import random
import os
import numpy as np
from scipy.io import wavfile
import pyaudio
import wave
import sys
import fcntl
import time
#%%
tone = ["Ab","A","A#","Bb","B","C","C#","Db","D","D#","Eb","E","F","F#"]
chord = ["M7","m7","7","m7b5"]
#%%


# %%
count = 0
print("flash chord evoker : start")
time.sleep(60/int(sys.argv[1]))
os.system("afplay /System/Library/Sounds/Pop.aiff")
print(".")
time.sleep(60/int(sys.argv[1]))
os.system("afplay /System/Library/Sounds/Pop.aiff")
print("..")
time.sleep(60/int(sys.argv[1]))
os.system("afplay /System/Library/Sounds/Tink.aiff")
print("...")
time.sleep(60/int(sys.argv[1]))
while count < int(sys.argv[2]):
    os.system("afplay /System/Library/Sounds/Pop.aiff")
    print(random.choice(tone) + random.choice(chord))
    count += 1
    time.sleep(60/int(sys.argv[1]))
    os.system("afplay /System/Library/Sounds/Pop.aiff")
    print(".")
    time.sleep(60/int(sys.argv[1]))
    os.system("afplay /System/Library/Sounds/Pop.aiff")
    print("..")
    time.sleep(60/int(sys.argv[1]))
    os.system("afplay /System/Library/Sounds/Tink.aiff")
    print("...")
    time.sleep(60/int(sys.argv[1]))
print("Finish")
os.system("afplay /System/Library/Sounds/Bottle.aiff")






# %%
