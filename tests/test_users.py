from api.users import get_user, get_users_list, create_user, update_user, patch_user, delete_user
from schemas import (
    USER_SCHEMA, 
    USER_LIST_SCHEMA, 
    USER_CREATE_SCHEMA, 
    USER_UPDATE_SCHEMA,
    USER_PATCH_SCHEMA,
    validate_schema
)

#유저 조회
def test_get_user_success():
    response = get_user(2)

    assert response.status_code == 200
    data = response.json()['data']
    assert "id" in data
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    
    # 스키마 검증
    assert validate_schema(data, USER_SCHEMA), "응답이 사용자 스키마와 일치하지 않습니다."

def test_get_user_not_found():
    response = get_user(99999)

    assert response.status_code == 404
    assert response.text == "{}"

# 유저 목록 조회
def test_get_users_list():
    response = get_users_list()
    
    assert response.status_code == 200
    data = response.json()
    assert "page" in data
    assert "per_page" in data
    assert "total" in data
    assert "total_pages" in data
    assert "data" in data
    assert isinstance(data["data"], list)
    
    # 스키마 검증
    assert validate_schema(data, USER_LIST_SCHEMA), "응답이 사용자 목록 스키마와 일치하지 않습니다."
    
    if data["data"]:
        user = data["data"][0]
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user

# 유저 생성
def test_create_user():
    response = create_user("morpheus", "leader")
    
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
    assert "createdAt" in data
    
    # 스키마 검증
    assert validate_schema(data, USER_CREATE_SCHEMA), "응답이 사용자 생성 스키마와 일치하지 않습니다."

# 유저 정보 수정
def test_update_user():
    response = update_user(2, "morpheus", "zion resident")
    
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "zion resident"
    assert "updatedAt" in data
    
    # 스키마 검증
    assert validate_schema(data, USER_UPDATE_SCHEMA), "응답이 사용자 수정 스키마와 일치하지 않습니다."

# 유저 정보 부분 수정
def test_patch_user():
    response = patch_user(2, "zion resident")
    
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == "zion resident"
    assert "updatedAt" in data
    
    # 스키마 검증
    assert validate_schema(data, USER_PATCH_SCHEMA), "응답이 사용자 부분 수정 스키마와 일치하지 않습니다."

# 유저 삭제
def test_delete_user():
    response = delete_user(2)
    
    assert response.status_code == 204