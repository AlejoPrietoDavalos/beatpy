from typing import List
import requests
from requests import Response

def process_audio(*, urls: List[str]) -> Response:
    url_api = "http://127.0.0.1:8000/process_audio"
    return requests.post(url_api, json={"urls": urls})

urls = [
    "https://www.youtube.com/watch?v=5ViMA_qDKTU", # Isolation
    "https://www.youtube.com/watch?v=ynPjt2_Rb4I", # El cieguito volador
    "https://www.youtube.com/watch?v=KzqWe7uYo_A", # World in my eyes - Depeche Mode.
    "https://www.youtube.com/watch?v=O8BLUzAxNmQ", # Naty Peluso - Buenos Aires
]

r = process_audio(urls=urls)
print(f"status_code={r.status_code}")
print(r.text)