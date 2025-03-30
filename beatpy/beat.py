from pathlib import Path

import librosa
import librosa.display
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from beatpy.plot import plot_wave, plot_spectrogram

__all__ = ["Beat"]

class BeatBase:
    """
    - TODO: librosa.time_to_frames
    - TODO: librosa.time_to_samples
    """
    def __init__(self, *, path_audio: Path):
        self.path_audio = path_audio
        self.name = self.path_audio.name

        y, sr = librosa.load(self.path_audio, sr=None)
        self.y: np.ndarray = y
        self.sr: float = sr

        self._tempo: np.ndarray = None
        self._beat_frames: np.ndarray = None
        self._beat_times: np.ndarray = None
        self._S: np.ndarray = None
        self._S_db: np.ndarray = None

    @property
    def tempo(self) -> np.ndarray:
        if self._tempo is None:
            self._update_tempo_beat_frames()
        return self._tempo

    @property
    def beat_frames(self) -> float:
        if self._beat_frames is None:
            self._update_tempo_beat_frames()
        return self._beat_frames

    @property
    def beat_times(self) -> np.ndarray:
        """ Convertir beat frames a tiempos en segundos"""
        if self._beat_times is None:
            self._beat_times = librosa.frames_to_time(self.beat_frames, sr=self.sr)
        return self._beat_times

    @property
    def S(self) -> np.ndarray:
        """ Transformada de Fourier de corta duración (STFT)"""
        if self._S is None:
            self._S = librosa.stft(self.y)
        return self._S

    @property
    def S_dD(self) -> np.ndarray:
        """ Magnitud de S en decibeles"""
        if self._S_db is None:
            self._S_db = librosa.amplitude_to_db(abs(self.S))
        return self._S_db

    def _update_tempo_beat_frames(self) -> None:
        tempo, beat_frames = librosa.beat.beat_track(y=self.y, sr=self.sr)
        self._tempo = tempo
        self._beat_frames = beat_frames

    def plot_wave(self, *, ax: Axes):
        plot_wave(ax=ax, y=self.y, sr=self.sr, title= f"Wave {self.name}")

    def plot_spectrogram(
            self, *, ax: Axes,
            vmin: float = None, vmax: float = None,
            color_xaxis: str = "black"
    ):
        plot_spectrogram(
            ax=ax, sr=self.sr, S_db=self.S_dD,
            title=f"Spectrogram {self.name}",
            vmin=vmin, vmax=vmax, color_xaxis=color_xaxis
        )


class Beat(BeatBase):
    def __init__(self, *, path_audio: Path):
        super().__init__(path_audio=path_audio)

    def _metronome(self):
        # Detectar el primer onset fuerte (inicio de la canción)
        onset_env: np.ndarray = librosa.onset.onset_strength(y=self.y, sr=self.sr)
        onset_frames: np.ndarray = librosa.onset.onset_detect(onset_envelope=onset_env, sr=self.sr)
        first_onset_time: np.float64 = librosa.frames_to_time(onset_frames, sr=self.sr)[0]

        # Ajustar los tiempos del metrónomo
        adjusted_beat_times: np.ndarray = self.beat_times - (self.beat_times[0] - first_onset_time)

        # Guardar el metrónomo como un click track
        click_track: np.ndarray = librosa.clicks(times=adjusted_beat_times, sr=self.sr, length=len(self.y))
        print(type(self.beat_times))
        print(type(onset_env))
        print(type(onset_frames))
        print(type(first_onset_time))
        print(type(adjusted_beat_times))
        print(type(click_track))

        sf.write("metronome_synced.wav", click_track, self.sr)

        print(f"Tempo estimado: {self.tempo} BPM")
        print(f"Primer onset detectado en: {first_onset_time:.2f} s")

        S = librosa.stft(self.y)  # Transformada de Fourier de corta duración
        S_db = librosa.amplitude_to_db(abs(S))  # Convertir a escala logarítmica

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_db, sr=self.sr, x_axis="time", y_axis="log")
        plt.colorbar(label="Intensidad (dB)")
        plt.title("Espectrograma")
        plt.show()
        return onset_env, onset_frames, first_onset_time, adjusted_beat_times, click_track
