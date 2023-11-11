import sounddevice as sd
import numpy as np

def play_sound(frequency, duration):
    fs = 44100  # Sampling rate
    t = np.linspace(0, duration, int(fs * duration), False)

    # Generate a sine wave with the given frequency
    x = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(x, samplerate=fs)
    sd.wait()
    print(f"<{frequency}")
    



note = {
  'C1': 261.63,    
    'C#1': 277.18,
    'D1': 293.66,
    'D#1': 311.13,
    'E1': 329.63,
    'F1': 349.23,
    'F#1': 369.99,
    'G1': 392.00,
    'G#1': 415.30,
    'A1': 440.00,
    'A#1': 466.16,
    'B1': 493.88,
    'C2': 523.25,    
    'C#2': 554.37,
    'D2': 587.33,
    'D#2': 622.25,
    'E2': 659.26,
    'F2': 698.46,
    'F#2': 739.99,
    'G2': 783.99,
    'G#2': 830.61,
    'A2': 880.00,
    'A#2': 932.33,
    'B2': 987.77,
    'C3': 1046.50,   
    'C#3': 1108.73,
    'D3': 1174.66,
    'D#3': 1244.51,
    'E3': 1318.51,
    'F3': 1396.92,
    'F#3': 1479.98,
    'G3': 1567.98,
    'G#3': 1661.22,
    'A3': 1760.00,
    'A#3': 1864.66,
    'B3': 1975.53,
    'AIR': 0000,
}

length = {
    'W': 2, # Whole Note
    'H': 1, # Half Note
    'Q': .5, # Quarter Note --- NOTES WONT PLAY FASTER THAN THIS
    'E': 0.25, # Eight Note
    'S': 0.05 # Sixteenth

}
def ytp():
    play_sound(note['E2'], length['E'])
    play_sound(note['E2'], length['E'])
    play_sound(note['E2'], length['E'])
    play_sound(note['AIR'], length['E'])
    play_sound(note['E2'], length['E'])
    play_sound(note['G2'], length['E'])
    play_sound(note['F2'], length['E'])
    play_sound(note['E2'], length['E'])
    play_sound(note['AIR'], length['E'])
    play_sound(note['F2'], length['E'])
    play_sound(note['F2'], length['E'])
    play_sound(note['F2'], length['E'])
    play_sound(note['AIR'], length['E'])
    play_sound(note['F2'], length['E'])
    play_sound(note['G2'], length['E'])
    play_sound(note['G2'], length['E'])
    play_sound(note['G2'], length['E'])
    play_sound(note['AIR'], length['E'])
    play_sound(note['A2'], length['E'])
    play_sound(note['G2'], length['E'])
    play_sound(note['F2'], length['E'])
# # SEVEN NATION ARMY WHITE STRIPES
def whitestripes():
    play_sound(0,1)
    play_sound(note['E2'], length['Q'])
    play_sound(note['E2'], length['E'])
    play_sound(note['G2'], length['E'])
    play_sound(note['E2'], length['E'])
    play_sound(note['D2'], length['E'])
    play_sound(note['C2'], length['H'])
    play_sound(note['B1'], length['H'])
    play_sound(0,.5)
    play_sound(note['E2'], length['Q'])
    play_sound(note['E2'], length['E'])
    play_sound(note['G2'], length['E'])
    play_sound(note['E2'], length['E'])
    play_sound(note['D2'], length['E'])
    play_sound(note['C2'], length['E'])
    play_sound(note['D2'], length['E'])
    play_sound(note['C2'], length['E'])
    play_sound(note['B1'], length['E'])


for x in range(2):
    whitestripes()

