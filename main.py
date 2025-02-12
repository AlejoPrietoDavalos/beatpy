from pathlib import Path
import os

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import uvicorn

from api.tools.youtube.download_audio import download_audio


path_data = Path(os.getenv("PATH_DATA", "data"))    # TODO: En el servidor colocar bien.
#----> FIXME: Borrar.
try:
    path_data.mkdir(exist_ok=True)
except:
    pass
#----> FIXME: Borrar.


app = FastAPI()


class URLRequest(BaseModel):
    url: str        # TODO: HttpUrl

@app.post("/process_audio")
def _process_audio(request: URLRequest):
    path_audio = download_audio(url=request.url, path_out=path_data)
    return {"message": "URL recibida", "url": request.url}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
