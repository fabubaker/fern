# This file was auto-generated by Fern from our API Definition.

import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt

from ....core.datetime_utils import serialize_datetime
from ...commons.types.debug_variable_value import DebugVariableValue
from .expression_location import ExpressionLocation
from .stack_information import StackInformation
from .submission_id import SubmissionId
from .traced_file import TracedFile


class TraceResponseV2(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    line_number: int = pydantic.Field(alias="lineNumber")
    file: TracedFile
    return_value: typing.Optional[DebugVariableValue] = pydantic.Field(alias="returnValue")
    expression_location: typing.Optional[ExpressionLocation] = pydantic.Field(alias="expressionLocation")
    stack: StackInformation
    stdout: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
