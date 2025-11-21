import json
from typing import Any

class BSConfig:

    def __init__(self, json_config_file_path: str):
        for k, v in json.load(open(json_config_file_path, "r")).items():
            setattr(self, k, v)

    def get_property(self, prop: str) -> Any:
        return getattr(self, prop)

    def has_property(self, prop: str) -> bool:
        return hasattr(self, prop)
