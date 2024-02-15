# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .exception_info import ExceptionInfo

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Exception_Generic(ExceptionInfo):
    type: typing.Literal["generic"]

    class Config:
        allow_population_by_field_name = True


class Exception_Timeout(pydantic.BaseModel):
    type: typing.Literal["timeout"]


"""
from seed.examples import Exception_Generic

Exception_Generic(
    type="generic",
    exception_type="Unavailable",
    exception_message="This component is unavailable!",
    exception_stacktrace="<logs>",
)
"""
Exception = typing.Union[Exception_Generic, Exception_Timeout]
