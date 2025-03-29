from typing import Literal
from pathlib import Path
import subprocess

T_Quality = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
DEFAULT_QUALITY = 0
FFMPEG = "ffmpeg"


class ConvertAudio:
    @staticmethod
    def _convert(*, path_in: Path, format_out: str, quality: T_Quality = DEFAULT_QUALITY, delete_old: bool = True) -> Path:
        if not path_in.exists():
            raise ValueError(f"El archivo {path_in} no existe.")
        
        path_out = path_in.with_suffix(f".{format_out}")
        subprocess.run([FFMPEG, "-i", str(path_in), "-q:a", str(quality), str(path_out)], check=True)
        if delete_old:
            path_in.unlink()
        return path_out

    @staticmethod
    def to_mp3(*, path_in: Path, quality: T_Quality = DEFAULT_QUALITY, delete_old: bool = True) -> Path:
        ConvertAudio._convert(path_in=path_in, format_out="mp3", quality=quality, delete_old=delete_old)
