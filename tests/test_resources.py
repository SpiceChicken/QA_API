from api.resources import get_resources_list, get_resource
from schemas import (
    RESOURCE_SCHEMA, 
    RESOURCE_LIST_SCHEMA,
    validate_schema
)

# 리소스 목록 조회
def test_get_resources_list():
    response = get_resources_list()
    
    assert response.status_code == 200
    data = response.json()
    assert "page" in data
    assert "per_page" in data
    assert "total" in data
    assert "total_pages" in data
    assert "data" in data
    assert isinstance(data["data"], list)
    
    # 스키마 검증
    assert validate_schema(data, RESOURCE_LIST_SCHEMA), "응답이 리소스 목록 스키마와 일치하지 않습니다."
    
    if data["data"]:
        resource = data["data"][0]
        assert "id" in resource
        assert "name" in resource
        assert "year" in resource
        assert "color" in resource
        assert "pantone_value" in resource

# 단일 리소스 조회
def test_get_resource_success():
    response = get_resource(2)
    
    assert response.status_code == 200
    data = response.json()["data"]
    assert "id" in data
    assert "name" in data
    assert "year" in data
    assert "color" in data
    assert "pantone_value" in data
    
    # 스키마 검증
    assert validate_schema(data, RESOURCE_SCHEMA), "응답이 리소스 스키마와 일치하지 않습니다."

def test_get_resource_not_found():
    response = get_resource(99999)
    
    assert response.status_code == 404
    assert response.text == "{}" 