from pathlib import Path

class PathsBeatpy:
    def __init__(self, *, youtube_id: str, path_root: Path):
        self.youtube_id = youtube_id

        self.root = path_root
        self.folder = path_root / self.youtube_id
        self.folder.mkdir(exist_ok=True)

        self.audio = self.folder / f"{self.youtube_id}.mp3"
        self.info = self.folder / "info.json"
        self.bass = self.folder / "bass.mp3"
        self.drums = self.folder / "drums.mp3"
        self.other = self.folder / "other.mp3"
        self.piano = self.folder / "piano.mp3"
        self.vocals = self.folder / "vocals.mp3"
