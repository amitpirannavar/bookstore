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
