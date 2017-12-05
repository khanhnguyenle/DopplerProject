import wave
import numpy as np

def pitch_shift(filename, shift):
    #Credit to Patrick Maupin url:https://stackoverflow.com/questions/43162121/python-convert-mono-wave-file-to-stereo
    wavin = wave.open(filename, 'r')
    para = list(wavin.getparams())
    para[3] = 0
    para = tuple(para)
    wavout = wave.open('output' + filename, 'w')
    wavout.setparams(para)

    fr = 1
    sz = wavin.getframerate() // fr  # Read and process 1/fr second at a time.
    # A larger number for fr means less reverb.
    c = int(wavin.getnframes() / sz)  # count of the whole file
    shift = int(shift) // fr  # shifting 100 Hz
    for num in range(c):
        da = np.fromstring(wavin.readframes(sz), dtype=np.int16)
        left, right = da[0::2], da[1::2]  # left and right channel
        lf, rf = np.fft.rfft(left), np.fft.rfft(right)
        lf, rf = np.roll(lf, shift), np.roll(rf, shift)
        #lf[0:shift], rf[0:shift] = 0, 0
        nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
        ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
        wavout.writeframes(ns.tostring())
    wavin.close()
    wavout.close()


if __name__ == '__main__':
    pitch_shift('sine.wav', 100)