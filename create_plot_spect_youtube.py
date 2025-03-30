from typing import List, cast
from dotenv import load_dotenv
load_dotenv()

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from beatpy.beat import Beat
from beatpy.youtube import Youtube
from const import path_extracted

# Definir colores personalizados
COLOR_BACKGROUND = "#212167"
COLOR_TEXT = "#9696f6"

def plot_spectrograms_by_youtube(*, youtube_id: str) -> None:
    youtube = Youtube(youtube_id=youtube_id, path_root=path_extracted)
    
    # Se levantan todos los audios.
    beats: List[Beat] = [Beat(path_audio=p) for p in youtube.paths.iter_spleeter_output()]
    if len(beats) != 6:
        raise ValueError("TODO: Manejar bien el plot.")
    
    # Se calcula el valor minimo y máximo de dB en los distintos audios.
    mins_dB, maxs_dB = [], []
    for beat in beats:
        mins_dB.append(beat.S_dD.min())
        maxs_dB.append(beat.S_dD.max())
    vmin, vmax = min(mins_dB), max(maxs_dB)

    # Crear figura y ejes
    fig, axes = plt.subplots(2, 3, figsize=(30, 10))

    # Cambiar el color de fondo de la figura
    fig.patch.set_facecolor(COLOR_BACKGROUND)

    k = 0
    for i in range(len(axes)):
        for j in range(len(axes[0])):
            beat = beats[k]
            k += 1
            ax = cast(Axes, axes[i, j])

            # Se grafican los espectrogramas.
            beat.plot_spectrogram(ax=ax, vmin=vmin, vmax=vmax, color_xaxis=COLOR_TEXT)
            ax.set_title(f"{beat.name}", color=COLOR_TEXT)  # Títulos en color claro
            ax.set_ylabel('Frequency [Hz]', color=COLOR_TEXT)      # Etiqueta de Y

            # Cambiar color a la barra, y fondo de los ejes.
            # Cambiar color de fondo de cada eje
            ax.set_facecolor(COLOR_BACKGROUND)
            ax.tick_params(axis='both', colors=COLOR_TEXT)
            cbar = ax.collections[0].colorbar
            cbar.ax.tick_params(labelcolor=COLOR_TEXT)

    # Ajustar espacio para el título
    plt.subplots_adjust(top=0.92)
    fig.suptitle('Spectrogram - Song: [Joy Division - Isolation]', fontsize=16, color=COLOR_TEXT)  # Título en color claro

    path_plots = youtube.paths.folder / "plots"
    path_plots.mkdir(exist_ok=True)
    
    # Guardar la figura
    fig.savefig(path_plots / f"spleeter_{youtube_id}.png", bbox_inches='tight')
    del fig

if __name__ == "__main__":
    plot_spectrograms_by_youtube(youtube_id="5ViMA_qDKTU")
