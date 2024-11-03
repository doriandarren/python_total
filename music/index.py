import mido
from mido import MidiFile, MidiTrack, Message

# Crear el archivo MIDI
midi = MidiFile()

# Crear pista para acordes
chords_track = MidiTrack()
midi.tracks.append(chords_track)

# Crear pista para bajo
bass_track = MidiTrack()
midi.tracks.append(bass_track)

# Crear pista para percusión
drums_track = MidiTrack()
midi.tracks.append(drums_track)

# Progresión de acordes jazzísticos
chord_progression = [
    [60, 63, 67, 70],  # Cm7
    [67, 71, 74, 77],  # G7
    [65, 68, 72, 75],  # Fm7
    [62, 66, 69, 72]   # D7
]
chord_duration = 960  # Duración de cada acorde en ticks

# Añadir acordes a la pista
for chord in chord_progression:
    for note in chord:
        chords_track.append(Message('note_on', note=note, velocity=50, time=0))
    chords_track.append(Message('note_off', note=chord[0], velocity=50, time=chord_duration))

# Bajo (notas fundamentales de cada acorde)
bass_notes = [60, 67, 65, 62]  # C, G, F, D
bass_duration = 960

for note in bass_notes:
    bass_track.append(Message('note_on', note=note, velocity=60, time=0))
    bass_track.append(Message('note_off', note=note, velocity=60, time=bass_duration))

# Patrón de percusión
kick_drum = 36
snare_drum = 38
drum_pattern = [(kick_drum, 0), (snare_drum, 480), (kick_drum, 960), (snare_drum, 1440)]
drum_duration = 480

for _ in range(4):  # Repetir el patrón 4 veces
    for note, time in drum_pattern:
        drums_track.append(Message('note_on', note=note, velocity=70, time=time))
        drums_track.append(Message('note_off', note=note, velocity=70, time=drum_duration))

# Guardar el archivo MIDI
midi.save('lofi_jazz_base.mid')
print("Archivo MIDI generado: lofi_jazz_base.mid")










# import mido
# import random
#
# # Configuración básica
# bpm = 120
# melody_length = 8  # Número de notas en la melodía
#
# # Calcula la duración de una nota en milisegundos
# ticks_per_beat = mido.bpm2tempo(bpm) // 500
#
# # Crea un nuevo archivo MIDI
# mid = mido.MidiFile()
# track = mido.MidiTrack()
# mid.tracks.append(track)
#
# # Añadir un mensaje de ajuste de tiempo
# track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(bpm)))
#
# # Genera notas aleatorias para la melodía
# for _ in range(melody_length):
#     note = random.randint(60, 72)  # Notas entre C4 y C5
#     track.append(mido.Message('note_on', note=note, velocity=64, time=0))
#     track.append(mido.Message('note_off', note=note, velocity=64, time=ticks_per_beat))
#
# # Guarda el archivo MIDI
# mid.save('melody.mid')
# print("Archivo MIDI generado: melody.mid")
