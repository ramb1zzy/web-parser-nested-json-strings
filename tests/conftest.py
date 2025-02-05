import pytest
from app.serivce import JSONWebSerializer

@pytest.fixture(scope="session")
def json_web_serializer():
    return JSONWebSerializer()
