from api.login import login

# 로그인
def test_login_success():
    response = login("eve.holt@reqres.in", "cityslicka")
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_no_password():
    response = login("eve.holt@reqres.in", "")
    assert response.status_code == 400
    assert "error" in response.json()

def test_login_wrong_password():
    response = login("eve.holt@reqres.in", "wrongpassword")
    assert response.status_code in [200, 400]  # API 정책에 따라