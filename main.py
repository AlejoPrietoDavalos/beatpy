import os

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from youtube.download_audio import Youtube, youtube_id_from_url
from const import path_extracted

app = FastAPI()


class URLRequest(BaseModel):
    url: str        # TODO: HttpUrl

@app.post("/process_audio")
def _process_audio(request: URLRequest):
    youtube = Youtube(
        youtube_id=youtube_id_from_url(url=request.url),
        path_out=path_extracted
    )
    youtube.download_audio()

    return {"message": "URL recibida", "url": request.url}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
