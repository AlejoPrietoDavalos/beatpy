from pathlib import Path
import os

path_data = Path(os.getenv("PATH_DATA"))    # TODO: En el servidor colocar bien.
path_extracted = path_data / "extracted"
path_data.mkdir(exist_ok=True)
path_extracted.mkdir(exist_ok=True)

COLOR_BACKGROUND = "#212167"
COLOR_TEXT = "#9696f6"
