"""
- Vocals (singing voice) / accompaniment separation (2 stems)
- Vocals / drums / bass / other separation (4 stems)
- Vocals / drums / bass / piano / other separation (5 stems)
"""
from typing import Literal, List
from pathlib import Path
import subprocess
import logging

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

app = FastAPI()

T_Stems = Literal[2, 4, 5]
ALLOWED_STEMS = (2, 4, 5)
DEFAULT_STEMS = 5


class URLRequest(BaseModel):
    youtube_id: str
    stems: T_Stems = 5

def run_spleeter(
        *,
        path_audio: Path,
        stems: T_Stems = DEFAULT_STEMS
) -> None:
    """
    - TODO: https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-models-up-to-16khz
    """
    path_root = Path("data") / "extracted"
    logger.info(f"- Run spleeter - path_audio={path_audio} -> path_out={path_root}")
    if stems not in ALLOWED_STEMS:
        raise ValueError(f"Invalid stem {stems}.")
    CMD_RUN_SPLEETER = (
        f"spleeter separate -p spleeter:{stems}stems "
        # Este crea la carpeta con el nombre del archivo de mp3.
        # Como ya existe por mi estructura de proyecto, entonces no hace nada.
        f"-o {path_root} "
        f"{path_audio}"
    )
    subprocess.run(["bash", "-c", CMD_RUN_SPLEETER])





@app.post("/separate")
def separate(request: URLRequest):
    """TODO: Seguridad con token."""
    return {"status": "done"}
