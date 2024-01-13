import requests



BASE_URL = "http://127.0.0.1:8080"

def test_method_a():
    response = requests.get(f"{BASE_URL}/methodA")
    assert response.status_code == 200
    assert response.text == "Method A called"

def test_method_b():
    response = requests.get(f"{BASE_URL}/methodB")
    assert response.status_code == 200
    assert response.text == "Method B called"

def test_method_c():
    response = requests.get(f"{BASE_URL}/methodC")
    assert response.status_code == 200
    assert response.text == "Method C called"

def test_method_d():
    response = requests.get(f"{BASE_URL}/methodD")
    assert response.status_code == 200
    assert response.text == "Method D called"

def test_method_e():
    response = requests.get(f"{BASE_URL}/methodE")
    assert response.status_code == 200
    assert response.text == "Method E called"
