import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# ---- Simulation d'un signal cardiaque ----
fs = 100  # fréquence d'échantillonnage (Hz)
t = np.linspace(0, 10, fs*10)  # 10 secondes
# signal sinusoïdal qui simule un rythme cardiaque ~75 BPM (1.25 Hz)
signal = 0.5 * np.sin(2 * np.pi * 1.25 * t) + 0.05 * np.random.randn(len(t))

# ---- Détection des pics (battements) ----
peaks, _ = find_peaks(signal, height=0.3, distance=fs/2)  # seuil et espacement min
nb_beats = len(peaks)

# ---- Calcul de la fréquence cardiaque ----
duration = t[-1] - t[0]
bpm = (nb_beats / duration) * 60

print(f"Nombre de battements détectés : {nb_beats}")
print(f"Fréquence cardiaque estimée : {bpm:.2f} BPM")

# ---- Affichage du signal + détection ----
plt.figure(figsize=(10,4))
plt.plot(t, signal, label="Signal cardiaque simulé")
plt.plot(t[peaks], signal[peaks], "ro", label="Pics détectés")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.title(f"Détection de la fréquence cardiaque (~{bpm:.1f} BPM)")
plt.legend()
plt.show()
