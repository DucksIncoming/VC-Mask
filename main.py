import pyaudio
import struct
import matplotlib.pyplot as plt
import numpy as np

audio = pyaudio.PyAudio()
BUFFER = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

DebugMode = True

def defineFormants():
    pass

def getMicAudio():
    global DebugMode

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=BUFFER,
        start=True
    )

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    stream.close()
    print("\n> Closing Audio...")
        
print("Listening...")
getMicAudio()