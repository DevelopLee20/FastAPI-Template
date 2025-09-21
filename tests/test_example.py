from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_main_root():
    response = client.get("/")
    assert response.status_code == 200


def test_error_handler():
    response = client.get("/test-error")
    assert response.status_code == 404
    assert response.json() == {
        "status": False,
        "message": "This is a test error from /test-error",
        "detail": None,
    }


def test_example_root():
    response = client.get("/example/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from Example Service!"}
