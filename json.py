from abc import ABC, abstractmethod
from dataclasses import dataclass

# from pydantic import BaseModel
from typing import NewType, Union
import ujson as json
from pathlib import Path

JsonSchemaString = NewType("JsonSchemaString", str)


@dataclass
class JsonSchema:
    _schema_dict: dict
    _schema_str: JsonSchemaString

    def __init__(self, schema: Union[str, dict]):
        # TODO: chk if this is a valid json schema
        # maybe use the approach from `outlines`: https://github.com/outlines-dev/outlines/blob/ed44a47d43ea21446812d891e77ef1e560b61868/outlines/generate/json.py#L46

        if isinstance(schema, str):
            self._schema_str = JsonSchemaString(schema)
            self._schema_dict = json.loads(schema)
        elif isinstance(schema, dict):
            self._schema_dict = schema
            self._schema_str = JsonSchemaString(json.dumps(schema))

    def as_schema_string(self) -> JsonSchemaString:
        return self._schema_str


def load_json_dict(json_path: Path) -> dict:
    with open(json_path, "r") as json_file:
        json_dict = json.load(json_file)

    return json_dict
