import pytest
import sys
import os
from pathlib import Path

# Add the parent directory to the system path
sys.path.insert(0, str(Path(file).resolve().parent.parent))

from app import app  # Now this should work

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Greeting App!' in response.data

def test_greeting(client):
    response = client.post('/', data={'name': 'Alice'})
    assert b'Hello, Alice!' in response.data