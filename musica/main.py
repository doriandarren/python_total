from midiutil import MIDIFile

# Crear archivo MIDI
midi = MIDIFile(1)  # Una pista
midi.addTempo(0, 0, 60)  # Ritmo relajado: 60 BPM

# Sección A: Acordes tranquilos
chords_A = [
    (48, 52, 55),  # C Major
    (50, 53, 57),  # D Minor
    (45, 48, 52),  # A Minor
    (43, 47, 50),  # G Major
]

# Sección B: Variación en los acordes
chords_B = [
    (48, 51, 55),  # C Major 7
    (50, 53, 57),  # D Minor 7
    (45, 48, 51),  # A Minor 7
    (43, 47, 50),  # G Major 7
]

# Acordes extendidos para ~5 minutos (80 compases)
start_time = 0
for i in range(40):  # Alternar entre A y B para un total de 80 compases
    chords = chords_A if i % 2 == 0 else chords_B
    for chord in chords:
        for note in chord:
            midi.addNote(0, 0, note, start_time, 4, 50)  # Acordes suaves y largos
        start_time += 4

# Melodía extendida (se repite durante 80 compases)
melody = [
    72, 74, 72, 71, None,  # Espacios entre notas para calma
    74, 76, None, 74, 72,  # Variaciones sutiles
    69, 71, None, 72, None  # Cierre suave
]

time = 0
for _ in range(10):  # Repetir la melodía 10 veces (~80 compases)
    for note in melody:
        if note is not None:
            midi.addNote(0, 1, note, time, 2, 40)  # Notas largas y suaves
        time += 2

# Ritmo mínimo (kick y snare espaciados)
kick = [0, 6]  # Bombo en los beats 1 y 4
snare = [12]   # Caja solo una vez por compás (beat 4)

for compas in range(80):  # 80 compases de ritmo mínimo
    for beat in kick:
        midi.addNote(0, 9, 36, compas * 4 + beat, 0.5, 40)  # Kick tenue
    for beat in snare:
        midi.addNote(0, 9, 38, compas * 4 + beat, 0.5, 30)  # Snare muy leve

# Guardar el archivo MIDI
with open("lofi_5min_tranquil.mid", "wb") as output_file:
    midi.writeFile(output_file)












"""
Esta ok esta
"""

# from midiutil import MIDIFile
#
# # Crear un archivo MIDI
# midi = MIDIFile(1)  # Una pista
# midi.addTempo(0, 0, 70)  # Ritmo más lento: 70 BPM
#
# # Acordes más suaves y sostenidos (compases 1-8)
# chords = [
#     (48, 52, 55, 60),  # C Major (en octavas bajas para calidez)
#     (50, 53, 57, 62),  # D Minor 7
#     (45, 48, 52, 57),  # A Minor
#     (43, 47, 50, 55),  # G Major
# ]
#
# start_time = 0
# for i in range(8):  # Repetir los acordes suavemente
#     chord = chords[i % len(chords)]
#     for note in chord:
#         midi.addNote(0, 0, note, start_time, 4, 60)  # Cada acorde dura 4 beats con menor intensidad
#     start_time += 4
#
# # Melodía simplificada y alargada (compases 1-8)
# melody = [72, 74, 76, 72, 69, 71, 72]  # Suave, notas separadas para un flujo tranquilo
# time = 0
# for note in melody:
#     midi.addNote(0, 1, note, time, 2, 50)  # Notas más largas (2 beats) y menos intensas
#     time += 2
#
# # Ritmo tenue (bombo y caja espaciados, sin hi-hats apretados)
# kick = [0, 4]  # Bombo en beats 1 y 3
# snare = [6]  # Caja en el beat 4 del compás
# for beat in kick:
#     midi.addNote(0, 9, 36, beat, 0.5, 50)  # Kick con menor intensidad
# for beat in snare:
#     midi.addNote(0, 9, 38, beat, 0.5, 40)  # Snare con volumen reducido
#
# # Guardar el archivo MIDI
# with open("lofi_80s_soft.mid", "wb") as output_file:
#     midi.writeFile(output_file)






