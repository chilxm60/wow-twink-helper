# utils.py
"""
Small JSON helpers for the twink tool.
This is intentionally minimal.
"""

try:
    import orjson

    def JSON_LOADS(data: bytes):
        """Parse JSON from bytes using orjson if available."""
        return orjson.loads(data)

    def JSON_DUMPS(obj) -> str:
        """Dump JSON to string using orjson if available."""
        return orjson.dumps(obj).decode("utf-8")

except ImportError:
    import json

    def JSON_LOADS(data: bytes):
        """Parse JSON from bytes using the standard json module."""
        return json.loads(data.decode("utf-8"))

    def JSON_DUMPS(obj) -> str:
        """Dump JSON to string using the standard json module."""
        return json.dumps(obj)
