import requests
from requests import Response

def process_audio(*, url: str) -> Response:
    url_api = "http://127.0.0.1:8000/process_audio"
    return requests.post(url_api, json={"url": url})

# Isolation
#url = "https://www.youtube.com/watch?v=5ViMA_qDKTU"

# Buddy Rich
#url = "https://www.youtube.com/watch?v=aIjVro15Dns"

# El cieguito volador
#url = "https://www.youtube.com/watch?v=ynPjt2_Rb4I"

# World in my eyes - Depeche Mode.
url = "https://www.youtube.com/watch?v=KzqWe7uYo_A"

r = process_audio(url=url)
print(f"status_code={r.status_code}")
print(r.text)