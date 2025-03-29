from typing import List
from dotenv import load_dotenv
import logging
import os
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from beatpy.youtube import Youtube, youtube_ids_from_urls
from beatpy.spleeter_cmd import get_cmd_run_spleeter, T_Stems
from beatpy.convert_audio import ConvertAudio
from const import path_extracted

logger = logging.getLogger(__name__)
app = FastAPI()


class URLRequest(BaseModel):
    urls: List[str]        # TODO: HttpUrl
    stems: T_Stems = 5

def process_audio(*, youtube_id: str, stems: T_Stems) -> None:
    logger.info(f"~~~~~ Process Audio - youtube_id={youtube_id} ~~~~~")
    youtube = Youtube(youtube_id=youtube_id, path_root=path_extracted)
    youtube.download_audio()
    # TODO: Ver si ya lo tenía descargado para enviarle el mismo.
    get_cmd_run_spleeter(
        path_root=youtube.paths.root,
        path_audio=youtube.paths.audio,
        stems=stems
    )
    for p in youtube.paths.folder.iterdir():
        if p.suffix == ".wav":
            ConvertAudio.to_mp3(path_in=p)


@app.post("/process_audio")
def _process_audio(request: URLRequest):
    for youtube_id, url in youtube_ids_from_urls(urls=request.urls):
        if youtube_id is None:
            logger.error(f"Invalid url {url}")
        process_audio(youtube_id=youtube_id, stems=request.stems)
    return {"message": "URLs recibida", "urls": f"{request.urls}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
