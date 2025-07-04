from datetime import timedelta
from bookstore.utils import create_access_token
import jwt
from bookstore.constants import SECRET_KEY, ALGORITHM


def test_create_access_token():
    data = {"sub": "test@example.com"}
    token = create_access_token(data, timedelta(minutes=5))
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded["sub"] == "test@example.com"
