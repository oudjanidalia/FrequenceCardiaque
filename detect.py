from signal_generator import generate_signal, load_signal_from_csv
from analysis import detect_heart_rate
from visualize import plot_signal

# ---- Paramètres ----
USE_CSV = False           # Passe à True pour analyser data/sample_signal.csv
CSV_PATH = 'data/sample_signal.csv'
FS = 100                  # Fréquence d'échantillonnage (Hz)
DURATION = 10             # Durée de la simulation (s)
BPM_TARGET = 78           # BPM simulé si USE_CSV=False

if __name__ == '__main__':
    # 1) Charger ou générer le signal
    if USE_CSV:
        t, signal = load_signal_from_csv(CSV_PATH, fs=FS)
    else:
        t, signal = generate_signal(fs=FS, duration=DURATION, bpm=BPM_TARGET)

    # 2) Détection de la FC
    nb_beats, bpm, peaks = detect_heart_rate(t, signal, fs=FS)

    # 3) Résultats console
    print(f"Nombre de battements détectés : {nb_beats}")
    print(f"Fréquence cardiaque estimée : {bpm:.2f} BPM")

    # 4) Visualisation
    plot_signal(t, signal, peaks, bpm)
