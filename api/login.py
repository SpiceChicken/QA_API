from api.config import make_request

# 로그인
def login(email, password):
    payload = {
        "email": email,
        "password": password
    }
    response = make_request("POST", "/api/login", json=payload)
    return response