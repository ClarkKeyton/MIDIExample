import python3_midi

def MIDI(midi_str_file : str):
    pattern = python3_midi.read_midifile("{}".format(midi_str_file))
    return pattern
if __name__ == "__main__":
    scanpat = MIDI("D:\\MIDI\\DragonBallGOKUULTRAINSTINCT.mid")
    print(scanpat)
    exit(454)