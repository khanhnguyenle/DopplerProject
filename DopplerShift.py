def shift(frequency, speed):
    c = 343 #Speed of sound is 343 m/s in air
    f = frequency * ((c + speed)/ c)
    return f

def velocity():
    #TODO Get that accelerometer working
    return 0;