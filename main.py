import pyaudio
import struct
import matplotlib.pyplot as plt
import numpy as np

audio = pyaudio.PyAudio()
BUFFER = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

DebugMode = True

def debugAnalyzer(data_int : int):
    pass


def getMicAudio():
    global DebugMode

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=BUFFER
    )

    try:
        while True:
            data = stream.read(BUFFER)
            data_int = struct.unpack(str(4 * BUFFER) + 'B', data)
            #print(data_int)

            if (DebugMode):
                debugAnalyzer(data_int)
    except KeyboardInterrupt:
        pass

    stream.close()
    print("\n> Closing audio...")

print("Listening...")
getMicAudio()