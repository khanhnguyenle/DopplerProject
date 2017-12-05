from pylab import*
from scipy.io import wavfile
from contextlib import suppress


def get_freq(filename):
    sampFreq, snd = wavfile.read(filename)
    snd = snd / (2.**15) #16 bit signed
    sample_points = snd.shape[0]
    s1 = snd[:, 0] #Use one channel
    n = len(s1)
    p = np.fft.fft(s1)  # take the fourier transform
    nUniquePts = int(ceil((n + 1) / 2.0))
    p = p[0:nUniquePts]
    p = abs(p)
    p = p / float(n)  # scale by the number of points so that
    # the magnitude does not depend on the length
    # of the signal or on its sampling frequency
    p = p ** 2  # square it to get the power
    if n % 2 > 0:
        p[1:len(p)] = p[1:len(p)] * 2
    else:
        p[1:len(p) - 1] = p[1:len(p) - 1] * 2
    with suppress(RuntimeWarning):
        p = 10 * log10(p)
    freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);
    #plot(freqArray / 1000, p, color='k')
    ymax = p[1:].argmax()
    xmax = freqArray[ymax] / 1000 #Ho ho ho, merry xmax
    #xlabel('Frequency (kHz)')
    #ylabel('Power (dB)')
    #plt.show()
    return xmax

if __name__ == '__main__':
    print(get_freq("outputsine.wav"))