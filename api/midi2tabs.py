from basic_pitch.inference import predict
import pretty_midi
import os 

def midi2tabs(file_path):

    dombyra_tabs = {}
    model_output, midi_data, note_events = predict(file_path)
    midi_data.write('./media/output.mid')

        
    midi_data = pretty_midi.PrettyMIDI("./media/output.mid")
  

    temp_tabs = []
    temp_duration = []
    low_notes_count = 0
    high_notes_count = 0
    for instrument in midi_data.instruments:

        for note in instrument.notes:

            temp_tabs.append(note.velocity)
            temp_duration.append(note.end - note.start)
            #print(f'Note: {note.pitch}, Start: {note.start}, End: {note.end}, Velocity: {note.velocity}')

    if len(temp_tabs) > 0:
        averageVelocity = sum(temp_tabs) / len(temp_tabs)
        averageTime = sum(temp_duration) / len(temp_duration)

        for instrument in midi_data.instruments:
            i = 0
            for note in instrument.notes:
                if note.velocity >= averageVelocity:
                    tab = (note.pitch - 55)
                    dombyra_tabs[i] = [tab, note.end - note.start]
                    i += 1

    return dombyra_tabs



