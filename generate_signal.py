import numpy as np
import pandas as pd

def generate_signal(fs=100, duration=10, bpm=75, noise=0.05, seed=42):
    rng = np.random.default_rng(seed)
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    freq_hz = bpm / 60.0
    signal = 0.6*np.sin(2*np.pi*freq_hz*t) + noise * rng.normal(size=t.shape)
    return t, signal

def load_signal_from_csv(path, fs=100):
    df = pd.read_csv(path)
    if 'signal' not in df.columns:
        raise ValueError("Le fichier CSV doit contenir une colonne 'signal'")
    signal = df['signal'].to_numpy()
    t = np.arange(len(signal)) / fs
    return t, signal
