from abc import ABC, abstractmethod
from dataclasses import dataclass

from pydantic import BaseModel
import ujson as json
from json import JsonSchema
# from typing import Any, Union, Optional, NewType, Generic


@dataclass
class DataModel(ABC):
    @abstractmethod
    def as_json_schema(self) -> JsonSchema:
        pass


@dataclass
class JsonSchemaDataModel(DataModel):
    _jsonschema: JsonSchema

    def __init__(self, schema: JsonSchema):
        self._jsonschema = schema

    def as_json_schema(self) -> JsonSchema:
        return self._jsonschema


@dataclass
class PydanticDataModel(DataModel):
    _model: BaseModel
    _jsonschema: JsonSchema

    def __init__(self, model: BaseModel):
        self._model = model

        model_dict: dict = self._model.model_json_schema(mode="validation")
        self._jsonschema = JsonSchema(model_dict)

    def as_json_schema(self) -> JsonSchema:
        return self._jsonschema
