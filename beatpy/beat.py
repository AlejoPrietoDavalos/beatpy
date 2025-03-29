from pathlib import Path
from typing import Tuple

import librosa
import librosa.display
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

from beatpy.plot import plot_wave, plot_spectrogram

__all__ = ["Beat"]

class BeatBase:
    """
    - TODO: librosa.time_to_frames
    - TODO: librosa.time_to_samples
    """
    def __init__(self, *, path_audio: Path):
        self.path_audio = path_audio
        y, sr = librosa.load(self.path_audio, sr=None)
        self.y: np.ndarray = y
        self.sr: float = sr

    def plot_wave(self):
        plot_wave(y=self.y, sr=self.sr)

    def plot_spectrogram(self):
        plot_spectrogram(y=self.y, sr=self.sr)

    def get_tempo_beat_frames(self) -> Tuple[float, np.ndarray]:
        tempo, beat_frames = librosa.beat.beat_track(y=self.y, sr=self.sr)
        return tempo, beat_frames


class Beat(BeatBase):
    def __init__(self, *, path_audio: Path):
        super().__init__(path_audio=path_audio)

    def _get_metronome(self):
        tempo, beat_frames = self.get_tempo_beat_frames()
        # Convertir beat frames a tiempos en segundos
        beat_times = librosa.frames_to_time(beat_frames, sr=self.sr)

        # Detectar el primer onset fuerte (inicio de la canción)
        onset_env = librosa.onset.onset_strength(y=self.y, sr=self.sr)
        onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=self.sr)
        first_onset_time = librosa.frames_to_time(onset_frames, sr=self.sr)[0]

        # Ajustar los tiempos del metrónomo
        adjusted_beat_times = beat_times - (beat_times[0] - first_onset_time)

        # Guardar el metrónomo como un click track
        click_track = librosa.clicks(times=adjusted_beat_times, sr=self.sr, length=len(self.y))

        # Guardar el audio combinado
        sf.write("metronome_synced.wav", click_track, self.sr)

        print(f"Tempo estimado: {tempo} BPM")
        print(f"Primer onset detectado en: {first_onset_time:.2f} s")

        S = librosa.stft(self.y)  # Transformada de Fourier de corta duración
        S_db = librosa.amplitude_to_db(abs(S))  # Convertir a escala logarítmica

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_db, sr=self.sr, x_axis="time", y_axis="log")
        plt.colorbar(label="Intensidad (dB)")
        plt.title("Espectrograma")
        plt.show()
