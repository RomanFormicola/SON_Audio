# SON_Audio
This is a new project that I am working which plays with audio in python. As of now the project uses the pyo 
python library for creating and manipulating sine waves. Most of the code written right now is in service of 
the "chord slide" instrument which takes in a 2D array of frequencies which corresponds to a list of chords and 
microtonally slides each note in each chord to the corresponding next note in the next chord outputting these sign waves
in real time and creating an audio file recording.

I have a lot of big goals with SON_Audio including instuments which analyze big data sets in order to define note intervals so that 
I can hear the Sound-of-Nature through listening to those data sets. There are all sorts of fun machine learning opertunities here and I can hopefully 
create some interesting art while learning.

To run son.py and hear an Amin -> Dmaj -> Fmin -> Emin7 -> Amin (omit 5) chord progression first install the dependencies in package-list.txt using Anaconda 
then execute:
    
    python son.py
