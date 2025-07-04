import pytest

@pytest.fixture
def auth_token(client):
    client.post("/signup", json={"email": "testbook@example.com", "password": "testpass"})
    response = client.post("/login", json={"email": "testbook@example.com", "password": "testpass"})
    return response.json()["access_token"]

def test_create_and_get_book(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    book_data = {
        "name": "Test Book",
        "author": "Author",
        "published_year": 2024,
        "book_summary": "Great book."
    }
    # Create
    create_resp = client.post("/books/", json=book_data, headers=headers)
    assert create_resp.status_code == 200
    created_book = create_resp.json()
    book_id = created_book["id"]

    # Get
    get_resp = client.get(f"/books/{book_id}", headers=headers)
    assert get_resp.status_code == 200
    assert get_resp.json()["name"] == "Test Book"
