from api.support import register_support, support_login
from schemas import (
    AUTH_SCHEMA, 
    REGISTER_SCHEMA, 
    ERROR_SCHEMA,
    validate_schema
)

# 지원 요청 등록
def test_register_support():
    response = register_support("eve.holt@reqres.in", "pistol")
    
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "token" in data
    
    # 스키마 검증
    assert validate_schema(data, REGISTER_SCHEMA), "응답이 등록 스키마와 일치하지 않습니다."

def test_register_support_failure():
    response = register_support("sydney@fife", "")
    
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    
    # 스키마 검증
    assert validate_schema(data, ERROR_SCHEMA), "응답이 에러 스키마와 일치하지 않습니다."

# 지원 요청 로그인
def test_support_login():
    response = support_login("eve.holt@reqres.in", "pistol")
    
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    
    # 스키마 검증
    assert validate_schema(data, AUTH_SCHEMA), "응답이 인증 스키마와 일치하지 않습니다."

def test_support_login_failure():
    response = support_login("peter@klaven", "")
    
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    
    # 스키마 검증
    assert validate_schema(data, ERROR_SCHEMA), "응답이 에러 스키마와 일치하지 않습니다." 