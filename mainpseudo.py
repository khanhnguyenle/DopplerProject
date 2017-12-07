if __name__ == '__main__':

    #AUDIO PROCESSING
    filename = "sine.wav"
    #record(filename)
    f = Frequency.get_freq(filename)
    print(f, "kHz")
    #play_back(filename)   ATTENTION: commented out, moved below
    fnew = DopplerShift.shift(f, 50)
    print(fnew, "kHz")
    PitchShift.pitch_shift(filename, (fnew - f) * 1000)
    print(Frequency.get_freq("output" + filename), "kHz")

    PitchShift.pitch_shift("output" + filename, - ((fnew - f) * 1000))  #this is to make the final product

    #AUDIO PLAYBACK
    play_back("first.wav")
    play_back(filename)
    play_back("second.wav")
    play_back("output" + filename)
    play_back("third.wav")
    play_back("output" + "output" + filename)                 #can be filename, or "output" + "output" + filename, both sounds the same
