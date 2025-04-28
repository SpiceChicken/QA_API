import requests

BASE_URL = "https://reqres.in"
HEADERS = {
    "x-api-key": "reqres-free-v1"
}

def make_request(method, endpoint, **kwargs):
    url = f"{BASE_URL}{endpoint}"
    kwargs['headers'] = HEADERS
    return requests.request(method, url, **kwargs) 