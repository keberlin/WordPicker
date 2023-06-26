import pytest

from app import create_app
from database import db


@pytest.fixture(scope="session", autouse=True)
def client():
    app = create_app()
    with app.app_context():
        app.testing = True
        yield app.test_client()
