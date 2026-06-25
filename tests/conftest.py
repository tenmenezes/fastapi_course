import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app

# ? Bloco de código de teste reutilizável


@pytest.fixture
def client():
    return TestClient(app)
