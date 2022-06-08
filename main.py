import pyaudio
import struct
import wave
import matplotlib.pyplot as plt
import numpy as np

audio = pyaudio.PyAudio()
BUFFER = 1
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

DebugMode = True

def pitchShift(audioIn, amount: float):
    audioIn = np.array(wave.struct.unpack("%dh"(len(audioIn) / amount)))

    audioIn = np.fft.rfft(audioIn)
    audioIn = np.roll(audioIn, amount)
    audioIn[0:amount] = 0
    audioIn = np.fft.irfft(audioIn)

    return audioIn

def formantShift(audioIn, gender: str):
    return audioIn

def getMicAudio():
    global DebugMode
    global audio

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
            data = stream.read(BUFFER)

            data = pitchShift(data, 100)
            #data = formantShift(data, "female")
            stream.write(data)
    except KeyboardInterrupt:
        pass

    stream.close()
    print("\n> Closing Audio...")
        
print("Listening...")
getMicAudio()