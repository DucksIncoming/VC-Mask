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

    fig, ax = plt.subplots()
    x = np.arange(0, 2 * BUFFER, 2)
    line, = ax.plot(x, np.random.rand(BUFFER))
    ax.set_xlim(0,255)
    ax.set_ylim(0, BUFFER)

    try:
        while True:
            data = stream.read(BUFFER)
            data_int = np.array(struct.unpack(str(4 * BUFFER) + 'B', data), dtype='b')[::2] + 127

            line.set_ydata(data_int)
            fig.canvas.draw()
            fig.canvas.flush_events()
    except KeyboardInterrupt:
        pass

    stream.close()
    print("\n> Closing audio...")

print("Listening...")
getMicAudio()