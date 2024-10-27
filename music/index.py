import mido
import random

# Configuración básica
bpm = 120
melody_length = 8  # Número de notas en la melodía

# Calcula la duración de una nota en milisegundos
ticks_per_beat = mido.bpm2tempo(bpm) // 500

# Crea un nuevo archivo MIDI
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

# Añadir un mensaje de ajuste de tiempo
track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(bpm)))

# Genera notas aleatorias para la melodía
for _ in range(melody_length):
    note = random.randint(60, 72)  # Notas entre C4 y C5
    track.append(mido.Message('note_on', note=note, velocity=64, time=0))
    track.append(mido.Message('note_off', note=note, velocity=64, time=ticks_per_beat))

# Guarda el archivo MIDI
mid.save('melody.mid')
print("Archivo MIDI generado: melody.mid")
