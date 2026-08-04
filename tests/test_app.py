from fastapi.testclient import TestClient

from dunossauro_fastapi.app import app

client = TestClient(app)
