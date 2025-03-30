""" Incluir la lógica de diferentes plots."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import librosa

def plot_wave(
        *,
        ax: Axes,
        y: np.ndarray,
        sr: float,
        title: str = "Wave"
) -> None:
    librosa.display.waveshow(y, ax=ax, sr=sr)
    ax.set_title(title)

def plot_spectrogram(
    *,
    ax: Axes,
    sr: float,
    S_db: np.ndarray,
    title: str = "Spectrogram",
    ylabel: str = "Frequency [Hz]",
    cmap: str = "magma",
    vmin: float = None,
    vmax: float = None,
    color_xaxis: str = "black"
) -> None:
    """Plotea un espectrograma con escala logarítmica de frecuencia en el eje especificado, 
    usando una escala de color definida por vmin y vmax."""
    img = librosa.display.specshow(
        S_db, ax=ax, sr=sr,
        x_axis="time", y_axis="log",
        cmap=cmap, vmin=vmin, vmax=vmax
    )
    ax.set_title(title)
    ax.set_ylabel(ylabel)

    # Cambiar el color del texto del eje horizontal (Time)
    ax.xaxis.label.set_color(color_xaxis)  # Color claro para el eje X (Tiempo)

    # Agregar barra de color con valores en dB
    plt.colorbar(img, ax=ax, format="%+2.0f dB")

