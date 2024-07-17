import mido
import pretty_midi

class MidiNote:
    def __init__(self, note, velocity, duration):
        self.note = note
        self.velocity = velocity
        self.duration = duration

    def __repr__(self):
        return f'(note={self.note}, velocity={self.velocity}, duration={self.duration})'



# Use the function
file_path = 'output.mid'


midi_file = pretty_midi.PrettyMIDI(file_path)

notes = []

for instrument in midi_file.instruments:
    for note in instrument.notes:
        #print(f'Note: {note.pitch}, Start: {note.start}, End: {note.end}, Velocity: {note.velocity}, duration: {note.duration}')
        notes.append(MidiNote(note.pitch, note.velocity, note.duration))
print(notes)


# print(midi_numbers)
# for num in midi_numbers:
#     print(num - 55)

