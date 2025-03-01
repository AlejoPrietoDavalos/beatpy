from typing import Optional
from pathlib import Path
from urllib.parse import urlparse
import re

import yt_dlp


def extract_youtube_id(*, url: str) -> Optional[str]:
    # Validar que la URL es de YouTube (sin importar el esquema http/https)
    parsed_url = urlparse(url)
    if parsed_url.netloc not in ['www.youtube.com', 'youtube.com']:
        return None

    # Buscar el ID del video en la URL
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None


def download_audio(url: str, path_out: Path) -> Path:
    youtube_id = extract_youtube_id(url=url)
    opciones = {
        "format": "bestaudio/best",
        "outtmpl": str(path_out / f"{youtube_id}.%(ext)s"),
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ]
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=True)

        from pprint import pprint
        print("----> ver esto...")
        pprint(info.get("requested_downloads")[0]["filepath"])
        print("----> ver esto...")

        #with open("info.json", "w") as f:
        #    import json
        #    json.dump(info, f)

        title = info.get("title", "unknown")
        path_audio = path_out / f"{title}.mp3"      # FIXME: Supone que es mp3. porque?
    return path_audio
