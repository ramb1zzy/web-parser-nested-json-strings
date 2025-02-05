class JSONWebSerializer:
    async def parse_string_to_valid_json(self, value):
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        pass
