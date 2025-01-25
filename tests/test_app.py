"""Unit tests for the Greeting App."""

import sys
from pathlib import Path
import pytest
from app import app

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture(name='test_client')
def fixture_test_client():

    """Fixture for testing with Flask test client."""

    app.config['TESTING'] = True

    with app.test_client() as client:

        yield client


def test_home_page(test_client):

    """Test the home page."""

    response = test_client.get('/')

    assert response.status_code == 200

    assert b'Welcome to the Greeting App!' in response.data


def test_greeting(test_client):

    """Test greeting functionality."""

    response = test_client.post('/', data={'name': 'Homelander'})

    assert b'Hello, Homelander!' in response.data
# End of test file
