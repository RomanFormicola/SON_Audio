from pyo import *
import hz
import instruments

s = Server()
s.recordOptions(dur=-1, filename="output.wav", fileformat=0, sampletype=0, quality=0.4)
s.boot()
s.start()
time.sleep(0.5)
s.recstart()

#Define # of output waves
f = Adsr(dur=0, attack=0.1, mul=0.1)
out_wavs = [Sine(freq=0, mul=f).out(),
            Sine(freq=0, mul=f).out(),
            Sine(freq=0, mul=f).out()]

f.play()

instruments.chordSlide(s, out_wavs, [ [hz.A4, hz.E4, hz.C4], 
                        [hz.D4, hz.Fs4, hz.A4], 
                        [hz.F4, hz.Gs4, hz.E4],
                        [hz.E4, hz.G4, hz.B4, hz.Ds4],
                        [hz.A4, hz.E3 ] ], f, 100, 0.5, 0.01, 1) 

#instruments.playLine(hz.all_notes, 0.5)



f.stop()

s.recstop()
time.sleep(0.5)
s.stop()