import pytest
from fastapi.testclient import TestClient

from dunossauro_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
