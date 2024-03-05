
from mido import MidiFile

midi = MidiFile('pirates_modified.mid', clip=True)
#index=0
#for msg in midi.tracks[1]:
#    if msg.type=="note_on":
#           if index%2==0:
#               del midi.tracks[1][index]
#                midi.save('pirates_modified.mid')
for track in midi.tracks:
    print(track)
#print(mid.tracks[0])
   




