import os

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from youtube.download_audio import Youtube, youtube_id_from_url
from spleeter_utils import get_cmd_run_spleeter
from const import path_extracted

app = FastAPI()
STEMS = 5


class URLRequest(BaseModel):
    url: str        # TODO: HttpUrl

@app.post("/process_audio")
def _process_audio(request: URLRequest):
    youtube = Youtube(
        youtube_id=youtube_id_from_url(url=request.url),
        path_out=path_extracted
    )
    # TODO: Ver si ya lo tenía descargado para enviarle el mismo.
    if not youtube.path_folder_video.exists():
        youtube.download_audio()

    get_cmd_run_spleeter(youtube_id=youtube.youtube_id, stems=STEMS)
    return {"message": "URL recibida", "url": request.url}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
