# This file was auto-generated by Fern from our API Definition.

import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt

from ........core.datetime_utils import serialize_datetime
from .test_case_function import TestCaseFunction
from .test_case_implementation_description import TestCaseImplementationDescription


class TestCaseImplementation(pydantic.BaseModel):
    description: TestCaseImplementationDescription
    function: TestCaseFunction

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
