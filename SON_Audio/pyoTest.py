from pyo import *
import time

s = Server()
s.recordOptions(dur=-1, filename="out.wav", fileformat=0, sampletype=0, quality=0.4)
s.boot()

s.recstart()

s.start()
time.sleep(1)
'''
for j in range(100):
    cs4.freq += 10
    e4.freq -= 10
    time.sleep(0.1)

    print(e4.freq)


 ''' 
f = Adsr(attack=0, decay=.2, sustain=5, release=0, dur=5, mul=.01)
a4 = Sine(freq=440, mul=f).out()

cs4 = Sine(freq=261, mul=f).out() 

e4 = Sine(freq=329, mul=f).out()

g4 = Sine(freq=392, mul=f).out()

b4 = Sine(freq=494*2, mul=f).out()

f.play()
time.sleep(3)
f.stop()

time.sleep(1)

f.play()
time.sleep(2)
s.stop()

s.recstop()
#amaj7add9 = [a4, cs4, e4, g4, b4]
#example(Harmonizer)