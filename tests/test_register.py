from api.register import register

# 회원가입
def test_register_success():
    response = register("eve.holt@reqres.in", "pistol")
    assert response.status_code == 200
    assert "id" in response.json()
    assert "token" in response.json()

def test_register_no_password():
    response = register("eve.holt@reqres.in", "")
    assert response.status_code == 400
    assert "error" in response.json()

def test_register_invalid_email():
    response = register("invalid.email@test.com", "1234")
    assert response.status_code in [200, 400]
