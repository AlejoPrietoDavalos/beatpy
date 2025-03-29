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
from beatpy.path_download import PathDownload
from beatpy.spleeter_cmd import get_cmd_run_spleeter

logger = logging.getLogger(__name__)
app = FastAPI()
STEMS = 5


class URLRequest(BaseModel):
    urls: List[str]        # TODO: HttpUrl


def process_audio(*, youtube_id: str) -> None:
    logger.info(f"~~~~~ Process Audio - youtube_id={youtube_id} ~~~~~")
    path_download = PathDownload(youtube_id=youtube_id)
    youtube = Youtube(youtube_id=youtube_id, path_download=path_download)
    youtube.download_audio()
    # TODO: Ver si ya lo tenía descargado para enviarle el mismo.
    get_cmd_run_spleeter(youtube_id=youtube.youtube_id, stems=STEMS)


@app.post("/process_audio")
def _process_audio(request: URLRequest):
    for youtube_id, url in youtube_ids_from_urls(urls=request.urls):
        if youtube_id is None:
            logger.error(f"Invalid url {url}")
        process_audio(youtube_id=youtube_id)
    return {"message": "URLs recibida", "urls": f"{request.urls}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
