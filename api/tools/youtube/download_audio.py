import yt_dlp

def download_audio(url: str, output_path="./data"):
    opciones = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ]
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

#url_video = "https://www.youtube.com/watch?v=GVcOIlITUR8"
#download_audio(url_video)