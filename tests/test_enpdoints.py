import pytest
from fastapi import status


class TestEnpdoints:
    @pytest.mark.parametrize(
        "json_string, result",
        [
            (
                "{\"paddingRight\":24,\"paddingLeft\":24,\"borderRadius\":32,\"backgroundColor\":\"layerFloor1\",\"overflow\":\"hidden\"}",
                {
                    "paddingRight": 24,
                    "paddingLeft": 24,
                    "borderRadius": 32,
                    "backgroundColor": "layerFloor1",
                    "overflow": "hidden",
                },
            ),
            (
                "{\"nested\":{\"key\":\"value\"},\"list\":[1,2,3],\"boolean\":true}",
                {
                    "nested": {"key": "value"},
                    "list": [1, 2, 3],
                    "boolean": True,
                },
            ),
        ],
    )
    async def test_parse_json(self, async_client, json_string, result):
        response = await async_client.post("/", data={"json_string": json_string})
        response_data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_data == result
