import matplotlib.pyplot as plt

def plot_signal(t, signal, peaks=None, bpm=None):
    plt.figure(figsize=(10,4))
    plt.plot(t, signal, label="Signal cardiaque")
    if peaks is not None:
        plt.plot(t[peaks], signal[peaks], "ro", label="Pics détectés")
    title = "Signal cardiaque"
    if bpm is not None:
        title += f" (~{bpm:.1f} BPM)"
    plt.title(title)
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()
