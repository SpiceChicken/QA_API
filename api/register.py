from api.config import make_request

# 회원가입
def register(email, password):
    payload = {
        "email": email,
        "password": password
    }
    response = make_request("POST", "/api/register", json=payload)
    return response