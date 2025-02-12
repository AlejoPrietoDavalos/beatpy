import requests
url = "http://127.0.0.1:8000/process_audio/"
url_isolation = "https://www.youtube.com/watch?v=5ViMA_qDKTU"
r = requests.post(url, json={"url": url_isolation})
print(r.text)