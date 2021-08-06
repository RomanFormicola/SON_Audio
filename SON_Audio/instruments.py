from pyo import *
import numpy as np
from threading import Thread
import hz

#With this version I want to change my approach to signal processing slightly.
#I would like to try allowing the user to define a number of output signals
#and then pass that output signal through the instruments e.g. chordSlide, panSlide, 
#either sequentially or simultaniously. This prevents the outputs from getting interupted on chordSlide return
#which will allow for more musicality. Every instrument should get an out_wav list as well as parameters for their 
#modificatio.


def playLine(notes_hz, delay):
    a = Sine(freq=0, mul=0.01).out()

    for note in notes_hz:
        a.freq = note
        print(note)
        time.sleep(delay)


def chordSlide(s, out_wavs, chords_hz, env, p, chord_sit, note_sit, loop_num):


    print(chords_hz) 

    for loop in range(loop_num):
        for i in range(len(chords_hz)):
            threads = []

            print(chords_hz[i])

            #add a out wave if needed
            if(len(chords_hz[i]) > len(out_wavs)):
                for j in range(len(chords_hz[i]) - len(out_wavs)):
                    out_wavs.append(Sine(freq=0, mul=env).out())
            
            #add a 0 frequency chord element if needed
            elif(len(chords_hz[i]) < len(out_wavs)):
                for j in range(len(out_wavs) - len(chords_hz[i])):
                    chords_hz[i].append(0)

            for j in range(len(chords_hz[i])):
                print("Sliding: ", out_wavs[j].freq, "to ", chords_hz[i][j])
                t = Thread(target=noteSlide, args=(s, out_wavs[j], chords_hz[i][j], p, note_sit))
                threads.append(t)
                t.start()

            for thread in threads:
                thread.join()

            time.sleep(chord_sit)

        #return to start if still looping.
        threads = []
        if(loop != loop_num - 1): 
            for i in range(len(chords_hz[0])):
                print("Sliding: ", out_wavs[i].freq, "to ", chords_hz[0][i])
                t = Thread(target=noteSlide, args=(s, out_wavs[i], chords_hz[0][i], p, note_sit))
                threads.append(t)
                t.start()
                
            for thread in threads:
                thread.join()
            
            time.sleep(chord_sit)
    

    return
            
def noteSlide(s, out_wavs, target_hz, p, note_sit):

    if(out_wavs.freq < target_hz):
        start = out_wavs.freq
        step = (target_hz - out_wavs.freq) / p

        for j in np.arange(start, target_hz, step):
            out_wavs.freq += step
            time.sleep(note_sit)

    elif(out_wavs.freq > target_hz):
        start = out_wavs.freq
        step = -((out_wavs.freq - target_hz) / p)
        for j in np.arange(start, target_hz, step):
            out_wavs.freq += step
            time.sleep(note_sit)
            
    out_wavs.freq = target_hz

    return

