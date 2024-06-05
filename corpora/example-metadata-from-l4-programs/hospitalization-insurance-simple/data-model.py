# generated by datamodel-codegen:
#   filename:  data-model.json
#   timestamp: 2024-06-05T14:10:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel


class Model(BaseModel):
    __root__: Any


class LifeAssured(BaseModel):
    policyActive: bool
    age: float


class Reason(Enum):
    sickness = 'sickness'
    accidental_injury = 'accidental injury'
    other = 'other'


class CauseOfHospitalization(Enum):
    skydiving = 'skydiving'
    military_service = 'military service'
    other = 'other'


class HospitalizationInformation(BaseModel):
    reason: Reason
    causeOfHospitalization: CauseOfHospitalization
