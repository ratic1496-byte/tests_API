import requests
BASE_URL = "https://postman-echo.com"

def test_simple_get():
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200

def test_get_with_params():
    params = {"text": "hello"}
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.json()["args"]["text"] == "hello"

# Тест 3: POST запрос с JSON данными. Проверяем, что данные дошли
def test_post_json():
    payload = {"id": 123}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    assert response.json()["json"]["id"] == 123


def test_post_form():
    payload = {"login": "admin"}
    response = requests.post(f"{BASE_URL}/post", data=payload)
    assert response.json()["form"]["login"] == "admin"


def test_headers():
    my_headers = {"my-token": "12345"}
    response = requests.get(f"{BASE_URL}/get", headers=my_headers)
    assert response.json()["headers"]["my-token"] == "12345"
