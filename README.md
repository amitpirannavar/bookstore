# Bookstore API

## Overview

This project is a simple Bookstore API built with FastAPI. It allows users to manage books and perform user authentication, including sign-up and login functionalities. The API uses JWT tokens for securing endpoints related to book management.

## Features

- **Book Management**: Users can create, update, delete, and retrieve books.
- **User Authentication**: Includes user sign-up and login functionalities.
- **Secure Endpoints**: Uses JWT tokens to secure book management endpoints.
- **Automated Testing**: Unit and integration tests included using `pytest`.
- **CI/CD**: Tests automatically run using GitHub Actions.
- **Code Coverage**: Codecov integration tracks test coverage.

## Technologies

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **SQLAlchemy / SQLModel**: SQL toolkit and ORM layer for Python.
- **Passlib**: Comprehensive password hashing library for Python.
- **JWT**: JSON Web Tokens for securely transmitting information between parties.
- **Pytest**: Testing framework.
- **httpx**: For making async HTTP calls in integration tests.
- **GitHub Actions**: For CI.
- **Codecov**: For code coverage tracking.

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/bookstore.git
    ```

2. Navigate to the project directory:
    ```bash
    cd bookstore
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the FastAPI server:
    ```bash
    uvicorn bookstore.main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000/health`

### API Endpoints

#### Book Management (JWT Protected)

- `POST /books/`: Create a new book
- `PUT /books/{book_id}`: Update a book by ID
- `DELETE /books/{book_id}`: Delete a book by ID
- `GET /books/{book_id}`: Get a book by ID
- `GET /books/`: Get all books

#### User Authentication

- `POST /signup`: Register a new user
- `POST /login`: Log in and receive an access token

#### Health Check

- `GET /health`: Check the health status of the API

### Running Using Docker

To run the app with Docker:

```bash
docker compose up --build -d
```

### Running Tests Locally
```bash
pytest tests --disable-warnings
```
### To run with code coverage:
```bash
pytest --cov=bookstore tests/
```
### Testing Strategy
Unit Tests
Test isolated logic such as models (UserCredentials, Book) and utility functions (create_access_token).

External dependencies like databases are avoided or mocked.

Located in: tests/unit/

### Integration Tests
Simulate real HTTP calls to API endpoints using httpx.AsyncClient.

Test full user flow: /signup, /login, and CRUD operations on /books/.

Token-based authentication is verified.

Located in: tests/integration/

### Reliability and Maintainability
Tests use reusable pytest fixtures (conftest.py)

Duplicate user issues are handled with dynamic test data (uuid)

Project uses pytest-cov for code coverage and GitHub Actions for automation.

### Challenges and Solutions
-- Duplicate emails on test rerun	> Used uuid.uuid4() to create unique test emails
-- Import/module errors during test >	Used PYTHONPATH=. and absolute imports (from bookstore...)
-- JWT-protected routes in tests	> Generated token dynamically from /login API