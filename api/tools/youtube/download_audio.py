from pathlib import Path

import yt_dlp


def download_audio(url: str, path_out: Path) -> Path:
    opciones = {
        "format": "bestaudio/best",
        "outtmpl": str(path_out / "%(title)s.%(ext)s"),
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ]
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "unknown")
        path_audio = path_out / f"{title}.mp3"      # FIXME: Supone que es mp3. porque?
    return path_audio
#url_video = "https://www.youtube.com/watch?v=GVcOIlITUR8"
#download_audio(url_video)