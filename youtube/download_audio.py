"""
- TODO: Averiguar si puedo controlar el suffix de una forma cómoda.
"""
from typing import Optional, List
from pathlib import Path
from urllib.parse import urlparse
import json
import re

from yt_dlp import YoutubeDL

T_YoutubeId = str
INDENT = 4

def youtube_id_from_url(*, url: str) -> Optional[T_YoutubeId]:
    # Validar que la URL es de YouTube (sin importar el esquema http/https)
    parsed_url = urlparse(url)
    if parsed_url.netloc not in ['www.youtube.com', 'youtube.com']:
        return None

    # Buscar el ID del video en la URL
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None


class Youtube:
    def __init__(self, *, youtube_id: str, path_out: Path):
        self.youtube_id: T_YoutubeId = youtube_id
        self.path_out: Path = path_out
        self.path_folder_video: Path = self.path_out / self.youtube_id
        self.path_audio: Optional[Path] = None  # Referencia absoluta extraída con la api.
        
        self.path_folder_video.mkdir(exist_ok=True) # Se crea el folder que contiene todos los datos.

    @property
    def url(self) -> str:
        return f"https://www.youtube.com/watch?v={self.youtube_id}"

    @property
    def path_info(self) -> Path:
        return self.path_folder_video / "info.json"

    def extract_info(self, *, ydl: YoutubeDL) -> dict:
        """ Extraigo y formateo el `yt_info` y """
        yt_info = ydl.extract_info(self.url, download=True)
        for field_to_delete in self.info_fields_to_delete():
            yt_info.pop(field_to_delete)
        
        # Guardo el path_audio, tiene `referencia absoluta`.
        self.path_audio = Path(yt_info["requested_downloads"][0]["filepath"])

        with open(self.path_info, "w") as f:
            json.dump(yt_info, f, indent=INDENT)

    def download_audio(self) -> None:
        """
        - Crea un folder en `path_out/<youtube_id>/<youtube_id>.mp3`.
        """
        with YoutubeDL(self.get_options_youtube_dl()) as ydl:
            yt_info = self.extract_info(ydl=ydl)
            # --> TODO: Se puede seguir procesando el yt_info.

    def get_options_youtube_dl(self) -> dict:
        return {
            "format": "bestaudio/best",
            "outtmpl": str(self.path_folder_video / f"{self.youtube_id}.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192"
                }
            ]
        }

    @staticmethod
    def info_fields_to_delete() -> List[str]:
        """ Campos para borrar del info, son pesados, ver si sirve el dato."""
        return [
            "formats",
            "thumbnails",
            "heatmap"       #TODO: heatmap -> Graficar esto. Creo que es la forma de las ondas.
        ]
