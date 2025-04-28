from api.config import make_request

# 지원 요청 등록
def register_support(email, password):
    payload = {
        "email": email,
        "password": password
    }
    response = make_request("POST", "/api/register", json=payload)
    return response 

# 지원 요청 로그인
def support_login(email, password):
    payload = {
        "email": email,
        "password": password
    }
    response = make_request("POST", "/api/login", json=payload)
    return response