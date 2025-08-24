import numpy as np
from scipy.signal import find_peaks

def detect_heart_rate(t, signal, fs=100):
    peaks, _ = find_peaks(signal, height=np.mean(signal) + 0.2*np.std(signal), distance=fs/2)
    nb_beats = len(peaks)
    duration = t[-1] - t[0]
    bpm = (nb_beats / duration) * 60 if duration > 0 else 0
    return nb_beats, bpm, peaks
