# Good amount of pitch-shifting code is stolen from PRABLANC P. because I didn't wanna do it myself.
# https://github.com/pprablanc/ppsrt

from pyaudio import PyAudio, paContinue, paFloat32
import readchar
import AudioEffect

IN = []
OUT = []
PITCH = 1.0

def main():
    global PITCH

    effect = AudioEffect.ProsodicModificationRealTime(44100, 'float32')
    effect.pitch_rate = PITCH
    BUFFER_PYAUDIO_SIZE = effect.mid_buffer_size

    def callback(in_data, frame_count, time_info, flag):
        global PITCH, IN, OUT
        in_data = effect.str2numpy(in_data)
        IN.append(in_data)
        out_data = effect.pitchshifting(in_data)
        OUT.append(out_data)
        out_data = effect.numpy2str(out_data)
        return out_data, paContinue

    pa = PyAudio()
    stream = pa.open(format = paFloat32,
                     channels = 1,
                     rate = 44100,
                     frames_per_buffer = BUFFER_PYAUDIO_SIZE,
                     input = True,
                     output = True,
                     stream_callback = callback)

    print("Listening...")
    keypress = readchar.readchar()

    print("Closing Audio...")
    stream.close()
    pa.terminate()

def setPitch(amount=1.0, alignFormants=False):
    global PITCH
    PITCH = amount
    
    if (alignFormants):
        pass

setPitch(1.5, False)
main()