import pytest
from fastapi.testclient import TestClient
import bookstore.main
from bookstore.database import SQLModel, engine, SessionLocal

@pytest.fixture(scope="module")
def client():
    SQLModel.metadata.create_all(engine)
    with TestClient(bookstore.main.app) as c:
        yield c

@pytest.fixture(scope="function")
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
