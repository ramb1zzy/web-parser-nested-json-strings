import json


class JSONWebParser:
    async def parse_json_recursive(self, value):
        if isinstance(value, list):
            return [await self.parse_json_recursive(item) for item in value]

        if isinstance(value, dict):
            return {
                key: await self.parse_json_recursive(val)
                for key, val in value.items()
            }

        if isinstance(value, str):
            while True:
                try:
                    parsed = json.loads(value)
                    value = parsed
                    if not isinstance(value, str):
                        break
                except json.JSONDecodeError:
                    break

            if isinstance(value, (dict, list)):
                return await self.parse_json_recursive(value)
            else:
                return value

        return value


def json_web_parser():
    yield JSONWebParser()
