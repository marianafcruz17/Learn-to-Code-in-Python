import requests

r = requests.get("http://www.google.com")
r.status_code
r.headers
r.headers["Date"]
r.text
