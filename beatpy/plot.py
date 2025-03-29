""" Incluir la lógica de diferentes plots."""
import numpy as np
import matplotlib.pyplot as plt
import librosa

def plot_wave(y: np.ndarray, sr: float):
    plt.figure(figsize=(20, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.title("Forma de onda")
    plt.show()

def plot_spectrogram(*, y: np.ndarray, sr: float):
    """ TODO: Abstraer los cálculos del plot"""
    S = librosa.stft(y)
    S_db = librosa.amplitude_to_db(abs(S))
    plt.figure(figsize=(20, 10))
    librosa.display.specshow(S_db, sr=sr, x_axis="time", y_axis="log")
    plt.colorbar()
    plt.title("Espectrograma")
    plt.show()

