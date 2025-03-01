import requests
url_api = "http://127.0.0.1:8000/process_audio"

# Isolation
#url = "https://www.youtube.com/watch?v=5ViMA_qDKTU"

# Buddy Rich
#url = "https://www.youtube.com/watch?v=aIjVro15Dns"

url = "https://www.youtube.com/watch?v=ToQS7BzGMYE"

r = requests.post(url_api, json={"url": url})
print(f"status_code={r.status_code}")
print(r.text)