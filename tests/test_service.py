import pytest


class TestJSONWebSerializer:
    @pytest.mark.parametrize(
        "string_to_serialize, result",
        [
            (
                r"{\"paddingRight\":24,\"paddingLeft\":24,\"borderRadius\":32,\"backgroundColor\":\"layerFloor1\",\"overflow\":\"hidden\"}",
                {
                    "paddingRight": 24,
                    "paddingLeft": 24,
                    "borderRadius": 32,
                    "backgroundColor": "layerFloor1",
                    "overflow": "hidden",
                },
            )
        ],
    )
    async def test_parse_string_to_valid_json(
        self, json_web_serializer, string_to_serialize, result
    ):
        decoded_string = await json_web_serializer.parse_string_to_valid_json(
            string_to_serialize
        )
        assert decoded_string == result
