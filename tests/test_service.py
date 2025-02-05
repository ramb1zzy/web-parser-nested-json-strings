import pytest
import asyncio
import json
from app.serivce import JSONWebParser


@pytest.mark.asyncio
class TestJSONWebParser:
    @pytest.mark.parametrize(
        "input_val, expected",
        [
            # 1) A string that is not valid JSON
            ("Just a simple string", "Just a simple string"),

            # 2) A simple JSON object
            ('{"key": "value"}', {"key": "value"}),

            # 3) Nested JSON strings (double nesting)
            (
                    '{"outerKey": "{\\"innerKey\\": \\"someValue\\"}"}',
                    {"outerKey": {"innerKey": "someValue"}}
            ),

            # 4) An already existing dict
            (
                    {"already": "dict", "num": 42},
                    {"already": "dict", "num": 42}
            ),

            # 5) A list containing JSON strings
            (
                    ['{"a": 1}', 'some text', '{"b": 2}'],
                    [{"a": 1}, "some text", {"b": 2}]
            ),

            # 6) A string that contains an array of JSON objects
            (
                    '[{"id":1}, {"id":2}]',
                    [{"id": 1}, {"id": 2}]
            ),

        ]
    )
    async def test_parse_json_recursive(self, input_val, expected, json_web_parser):
        """
        These are tests for simple, valid JSON strings, including double nesting.
        """
        result = await json_web_parser.parse_json_recursive(input_val)
        assert result == expected

    @pytest.mark.asyncio
    async def test_deeply_nested_json(self, json_web_parser):
        """
        Example with a string that has 3+ levels of nested JSON,
        all properly escaped so each level is valid.
        """
        # Explanation of the nesting:
        # 1) Outermost layer: {"lvl1": "..."}
        # 2) Inside that string: {"lvl2": "..."}
        # 3) Another string: {"lvl3": {"foo": "bar"}}
        #
        # NOTE: The key is that each internal JSON is valid, with correct backslashes.
        data = (
            '{"lvl1":'
            ' "{\\"lvl2\\": '
            '\\"{\\\\\\"lvl3\\\\\\": {\\\\\\"foo\\\\\\": \\\\\\"bar\\\\\\"}}\\"}'
            '"}'
        )

        # Desired final result:
        expected = {
            "lvl1": {
                "lvl2": {
                    "lvl3": {
                        "foo": "bar"
                    }
                }
            }
        }
        result = await json_web_parser.parse_json_recursive(data)
        assert result == expected
