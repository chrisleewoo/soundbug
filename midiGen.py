
"""


"""
import constants
import containers
import events
import fileio
import sequencer
import util

global Tempo
global Notelength

global pop_ins
global rotate_ins
global load_ins
global store_ins
global get_ins
global break_ins
global continue_ins
global delete_ins
global make_ins
global import_ins
global bit_ins



# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = containers.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
track = containers.Track()
# Append the track to the pattern
pattern.append(track)
events.EndOfTrackEvent(tick=1, data =[])
# Instantiate a MIDI note on event, append it to the track
#on = events.NoteOnEvent(tick=0, velocity=20, pitch=64)
#track.append(on)
# Instantiate a MIDI note off event, append it to the track
#off = events.NoteOffEvent(tick=100, pitch=64)
#track.append(off)

Dict = {1: 'LOAD', 2: 'STORE', 3:'POP', 4: 'ROT', 5: 'GET', 6: 'BREAK', 7: 'CONT', 8: 'DEL', 9: 'BUILD', 10: 'IMPORT', 11: 'INPLACE'}

track.append(events.SetTempoEvent(tick=0, bpm = 130))
#change these according to preference
Tempo= 2
Notelength = 2

pop_ins =   115   #Agogo
pop_pitch = 43

rotate_ins = 19         #Church organ
rotate_pitch = 67

load_ins = 115      #woodblock #these push unto stack
load_pitch = 31

store_ins = 126     #Applause
store_pitch = 84

get_ins = 71            #Clarinet
get_pitch = 45

break_ins = 36          #Bass
break_pitch = 28

continue_ins = 22   #Harmonica
continue_pitch = 64

delete_ins = 120    #Fret noise
delete_pitch = 52

make_ins = 115           #woodblock push unto stack       
slice_pitch = 31

import_ins = 55    #orchestra hit
import_pitch = 76

bit_ins = 80        #Square waves!
bit_pitch = 60

def pop_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 0, value = pop_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=0, tick=ticktime, velocity=120, pitch=pop_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=pop_pitch, channel=0 )                               
    track.append(off)
    return ticktime

def rotate_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 1, value = rotate_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=1, tick=ticktime, velocity=120, pitch=rotate_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=rotate_pitch, channel=1 )
    track.append(off)
    return ticktime 

def load_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 2, value = load_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=2, tick=ticktime+Tempo, velocity=120, pitch=load_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=load_pitch, channel=2 )
    track.append(off)
    return ticktime 

def store_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 3, value = store_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=3, tick=ticktime+Tempo, velocity=120, pitch=store_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=store_pitch, channel=3 )
    track.append(off)
    return ticktime 

def get_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 4, value = get_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=4, tick=ticktime+Tempo, velocity=120, pitch=get_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=get_pitch, channel=4 )
    track.append(off)
    return ticktime 
    
def break_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 5, value = break_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=5, tick=ticktime+Tempo, velocity=120, pitch=break_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=break_pitch, channel=5 )
    track.append(off)
    return ticktime 

def continue_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 6, value = continue_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=6, tick=ticktime+Tempo, velocity=120, pitch=continue_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=continue_pitch, channel=6 )
    track.append(off)
    return ticktime 

def delete_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 7, value = delete_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=7, tick=ticktime+Tempo, velocity=120, pitch=delete_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=delete_pitch, channel=7 )
    track.append(off)
    return ticktime 

def slice_sound(ticktime):
    #cc= events.ProgramChangeEvent(tick=0, channel = 8, value = make_ins)
    #track.append(cc)
    
    #root
    #on=events.NoteOnEvent(channel=8, tick=ticktime+Tempo, velocity=120, pitch=slice_pitch)
    #track.append(on)
    #ticktime+=Notelength+Tempo
    #off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=slice_pitch, channel=8 )
    #track.append(off)

    #3rd
    #on=events.NoteOnEvent(channel=8, tick=0, velocity=120, pitch=slice_pitch+4)
    #track.append(on)
    #ticktime+=Notelength+Tempo
    #off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=slice_pitch+4, channel=8 )
    #track.append(off)

    #5th
    #on=events.NoteOnEvent(channel=8, tick=0, velocity=120, pitch=slice_pitch+7)
    #track.append(on)
    #ticktime+=Notelength+Tempo
    #off=events.NoteOffEvent( tick= ticktime, pitch=slice_pitch+7, channel=8 )
    #track.append(off)
    #off=events.NoteOffEvent( tick= ticktime, pitch=slice_pitch, channel=8 )
    #track.append(off)
    #off=events.NoteOffEvent( tick= ticktime, pitch=slice_pitch+4, channel=8 )
    #track.append(off)


    return ticktime 

def import_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 9, value = import_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=9, tick=ticktime+Tempo, velocity=120, pitch=import_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=import_pitch, channel=9 )
    track.append(off)
    return ticktime 

def bit_sound(ticktime):
    cc= events.ProgramChangeEvent(tick=0, channel = 10, value = bit_ins)
    track.append(cc)
    on=events.NoteOnEvent(channel=10, tick=ticktime+Tempo, velocity=120, pitch=bit_pitch)
    track.append(on)
    #ticktime+=Notelength+Tempo
    off=events.NoteOffEvent( tick= ticktime+Notelength+Tempo, pitch=bit_pitch, channel=10 )
    track.append(off)
    return ticktime 


BREAK = ['BREAK', 'JUMP', 'CALL']
MAKE = ['BUILD', 'MAKE']
BITS = ['INPLACE', 'BINARY', 'UNARY', 'DUP']

with open('trace2Dis.dat') as t2D:
    cnt=25
    for line in t2D:
        #read_line = t2D.readline()
        if (line == '**EOD**'):
            t2D.close()
            break
        
        #process as a midi event
        t=line.split()
        try: msg_pitch = int(t[2])
        except: msg_pitch = 30
        try:
            current = (t[1])
            print current
        except:
            print('All Done!')
            break

        if ('LOAD' in t[1]):
            cnt = load_sound(cnt)
            print "~~LOAD"

        if ('STORE' in t[1]):
            cnt = store_sound(cnt)
            print "~~STORE"

             
        if ('POP' in t[1]):
            cnt = pop_sound(cnt)
            print "~~POP"

        if ('ROT' in t[1]):
            cnt = rotate_sound(cnt)
            print "~~ROT"

        if ('GET' in t[1]):
            cnt = get_sound(cnt)
            print "~~GET"

        if ('CONT' in t[1]):
            cnt = continue_sound(cnt)
            print "~~CONT"

        if ('DEL' in t[1]):
            cnt = delete_sound(cnt)
            print "~~DELETE"

        if ('IMPORT' in t[1]):
            cnt = import_sound(cnt)
            print "~~IMPORT"

        if ('SLICE' in t[1]):
            cnt = slice_sound(cnt)
            print "~~SLICE"

        for i in BREAK:
            if ( i in t[1]):
                cnt = break_sound(cnt)
                print "~~BREAK"

        for i in MAKE:
            if (i in t[1] ):
                cnt = load_sound(cnt)  # same as load
                print "~~PUSH (MAKE)"

        for i in BITS:
            if (i in t[1] ):
                cnt = bit_sound(cnt)
                print "~~BITOP"
            



# Add the end of track event, append it to the track
eot = events.EndOfTrackEvent(tick=1)
track.append(eot)
# Print out the pattern
#print pattern
# Save the pattern to disk
fileio.write_midifile("quick_sort.mid", pattern)

#pattern = fileio.read_midifile('example.mid')
#print pattern
