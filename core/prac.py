import json

import requests

url = "http://echo.jsontest.com/title/ipsum/content/blah"
response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
    speak_output = data['title']
else:
    data = json.loads(response.text)
    speak_output = data['title']


print(speak_output)
