# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt

from ....core.datetime_utils import serialize_datetime


class KeyValuePair(pydantic.BaseModel):
    key: VariableValue
    value: VariableValue

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


from .variable_value import VariableValue  # noqa: E402

KeyValuePair.update_forward_refs()
