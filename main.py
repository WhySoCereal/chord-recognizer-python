import rtmidi
from music21 import *

midi_in = rtmidi.RtMidiIn()

x = chord.Chord("C E G B")
print(x.pitchedCommonName)


def print_message(midi):
    if midi.isNoteOn():
        print('ON: ', midi.getMidiNoteName(midi.getNoteNumber()), midi.getVelocity())
    elif midi.isNoteOff():
        print('OFF:', midi.getMidiNoteName(midi.getNoteNumber()))
    elif midi.isController():
        print('CONTROLLER', midi.getControllerNumber(), midi.getControllerValue())


ports = range(midi_in.getPortCount())

if ports:
    for i in ports:
        print(midi_in.getPortName(i))
    print("Opening port 0!")
    midi_in.openPort(0)
    while True:
        m = midi_in.getMessage(250)  # some timeout in ms
        if m:
            print_message(m)
else:
    print('NO MIDI INPUT PORTS!')

