import pytest
import uuid

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

def test_access_books_without_token(client):
    response = client.get("/books/")
    assert response.status_code == 403
    assert response.json()["detail"] == "Not authenticated"

def test_book_crud_flow(client):
    # Sign up and get token
    email = f"bookuser_{uuid.uuid4().hex}@example.com"
    data = {"email": email, "password": "testpass"}
    client.post("/signup", json=data)
    token = client.post("/login", json=data).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create book
    book = {
        "name": "FastAPI",
        "author": "Amit",
        "published_year": 2024,
        "book_summary": "Great book"
    }
    create_res = client.post("/books/", json=book, headers=headers)
    assert create_res.status_code == 200
    created_book = create_res.json()
    book_id = created_book["id"]

    # Get book by ID
    get_res = client.get(f"/books/{book_id}", headers=headers)
    assert get_res.status_code == 200
    assert get_res.json()["name"] == "FastAPI"

    # Delete book
    delete_res = client.delete(f"/books/{book_id}", headers=headers)
    assert delete_res.status_code == 200
    assert delete_res.json()["message"] == "Book deleted successfully"
