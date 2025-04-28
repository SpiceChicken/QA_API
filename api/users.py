from api.config import make_request

#유저 조회
def get_user(user_id):
    response = make_request("GET", f"/api/users/{user_id}")
    return response

# 유저 목록 조회
def get_users_list():
    response = make_request("GET", "/api/users")
    return response

# 유저 생성
def create_user(name, job):
    payload = {
        "name": name,
        "job": job
    }
    response = make_request("POST", "/api/users", json=payload)
    return response

# 유저 정보 수정
def update_user(user_id, name, job):
    payload = {
        "name": name,
        "job": job
    }
    response = make_request("PUT", f"/api/users/{user_id}", json=payload)
    return response

# 유저 정보 부분 수정
def patch_user(user_id, job):
    payload = {
        "job": job
    }
    response = make_request("PATCH", f"/api/users/{user_id}", json=payload)
    return response

# 유저 삭제
def delete_user(user_id):
    response = make_request("DELETE", f"/api/users/{user_id}")
    return response