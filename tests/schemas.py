from jsonschema import validate

# 사용자 스키마
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string", "format": "email"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"}
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"]
}

# 사용자 목록 응답 스키마
USER_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": USER_SCHEMA
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}

# 사용자 생성/수정 응답 스키마
USER_CREATE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "job": {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": ["id", "name", "job", "createdAt"]
}

# PUT 요청 응답 스키마
USER_UPDATE_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
    "required": ["name", "job", "updatedAt"]
}

# PATCH 요청 응답 스키마
USER_PATCH_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
    "required": ["updatedAt"]  # PATCH는 부분 업데이트이므로 updatedAt만 필수
}

# 리소스 스키마
RESOURCE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "year": {"type": "integer"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"}
    },
    "required": ["id", "name", "year", "color", "pantone_value"]
}

# 리소스 목록 응답 스키마
RESOURCE_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": RESOURCE_SCHEMA
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}

# 로그인/등록 응답 스키마
AUTH_SCHEMA = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}

REGISTER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "token": {"type": "string"}
    },
    "required": ["id", "token"]
}

# 에러 응답 스키마
ERROR_SCHEMA = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

def validate_schema(data, schema):
    """응답 데이터가 스키마에 맞는지 검증합니다."""
    try:
        validate(instance=data, schema=schema)
        return True
    except Exception as e:
        print(f"스키마 검증 실패: {e}")
        return False 