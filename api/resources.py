from api.config import make_request

# 리소스 목록 조회
def get_resources_list():
    response = make_request("GET", "/api/unknown")
    return response

# 단일 리소스 조회
def get_resource(resource_id):
    response = make_request("GET", f"/api/unknown/{resource_id}")
    return response