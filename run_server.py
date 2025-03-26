import logging
import os
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from youtube.download_audio import Youtube, youtube_id_from_url
from src.path_download import PathDownload
from src.spleeter_utils import get_cmd_run_spleeter

logger = logging.getLogger(__name__)
app = FastAPI()
STEMS = 5


class URLRequest(BaseModel):
    url: str        # TODO: HttpUrl

@app.post("/process_audio")
def _process_audio(request: URLRequest):
    logger.info(f"~~~~~ request.url={request.url} ~~~~~")

    youtube_id = youtube_id_from_url(url=request.url)
    if youtube_id is None:
        raise HTTPException(status_code=404, detail="Invalid url.")

    path_download = PathDownload(youtube_id=youtube_id)
    youtube = Youtube(youtube_id=youtube_id, path_download=path_download)
    youtube.download_audio()
    # TODO: Ver si ya lo tenía descargado para enviarle el mismo.

    get_cmd_run_spleeter(youtube_id=youtube.youtube_id, stems=STEMS)
    return {"message": "URL recibida", "url": request.url}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
