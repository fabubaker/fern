# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt

from ......core.datetime_utils import serialize_datetime


class TestCaseTemplateId(pydantic.BaseModel):
    __root__: str

    def get_as_str(self) -> str:
        return self.__root__

    @staticmethod
    def from_str(value: str) -> TestCaseTemplateId:
        return TestCaseTemplateId(__root__=value)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
