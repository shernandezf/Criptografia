from mido import MidiFile

midi = MidiFile('piratasMod.mid', clip=True)
#index=0
#for msg in midi.tracks[1]:
#    if msg.type=="note_on":
#           if index%2==0:
#               del midi.tracks[1][index]
#                midi.save('pirates_modified.mid')
for msg in midi.tracks[0]:
    print(msg.type)
    if msg.type == "sysex":
        print(len(msg.data))
        
    print("---")
#print(mid.tracks[0])
