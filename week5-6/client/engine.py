import requests

URL = "http://server:8080/explain?prompt="
def explain(prompt):
    res = requests.get(URL+prompt)
    return res.json()["message"]
