from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.post("/analyze", files={"image": ("test.png", b"fakeimage", "image/png")})
    assert response.status_code == 200
    assert "extracted_text" in response.json()
    assert "analysis" in response.json()
