import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from app.serivce import JSONWebParser
import aiofiles
import json

@pytest.fixture(scope="session")
def json_web_parser():
    return JSONWebParser()


@pytest.fixture(scope="session")
def async_client():
    return AsyncClient(transport=ASGITransport(app), base_url="http://localhost:8000")

@pytest.fixture(scope="session")
async def json_test_data():
    async with aiofiles.open("package.json", mode="r") as f:
        return json.loads(await f.read())