import pytest
import uuid

def test_signup_and_login(client):
    # Sign Up
    unique_email = f"testuser_{uuid.uuid4().hex}@example.com"
    signup_data = {"email": unique_email, "password": "testpass"}
    response = client.post("/signup", json=signup_data)
    assert response.status_code == 200

    # Login
    response = client.post("/login", json=signup_data)
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data

def test_signup_duplicate_email(client):
    data = {"email": "duplicate@example.com", "password": "pass"}
    response1 = client.post("/signup", json=data)
    response2 = client.post("/signup", json=data)
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Email already registered"

def test_login_wrong_password(client):
    data = {"email": "wrongpass@example.com", "password": "correctpass"}
    client.post("/signup", json=data)

    bad_data = {"email": "wrongpass@example.com", "password": "wrongpass"}
    response = client.post("/login", json=bad_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect email or password"
