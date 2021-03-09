import time
import sys
import random
from mingus.midi import fluidsynth
from mingus.containers.note import Note


if len(sys.argv) != 3:
  print("usage: python lh_voicing.py <bpm> <path_to_sf2_file>")
  sys.exit(1)

fluidsynth.init(sys.argv[2], "coreaudio")

octave = '2'
time_between_tick = 60.0/int(sys.argv[1])
chords = [chr(ord('A') + i) for i in range(7)]
chords += ["Ab", "Bb", "Db", "Eb", "Gb"]
types = ["Maj7", "-7", "7", "-7b5", "Alt"]
#types = ["Maj7", "7"]
chords = set([a+b for a in chords for b in types])
count = 0
prev_root = ''
root = ''
while True:
  if count == 0:
    chord = random.sample(chords, 1)[0]
    prev_root = root
    root = chord[0:2] if chord[1] == 'b' else chord[0]
    if prev_root != '':
      n = Note(name=prev_root, octave=2)
      fluidsynth.play_Note(n)
    print(chord)
  else:
    print(".")
  count = (count + 1) % 4
  # sleep to time bpm, but also because fluidsynth
  # requires sleeping to play a note, for some reason
  time.sleep(time_between_tick)
