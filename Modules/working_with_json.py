import requests

r = requests.get("https://opentdb.com/api.php")
r.status_code
r.text
type(r.text)

import json

question = json.loads(r.text)
question
type(question)
