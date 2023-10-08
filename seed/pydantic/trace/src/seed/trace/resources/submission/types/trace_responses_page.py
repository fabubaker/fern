# This file was auto-generated by Fern from our API Definition.

import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt

from ....core.datetime_utils import serialize_datetime
from .trace_response import TraceResponse


class TraceResponsesPage(pydantic.BaseModel):
    offset: typing.Optional[int] = pydantic.Field(
        description=(
            "If present, use this to load subseqent pages.\n"
            "The offset is the id of the next trace response to load.\n"
        )
    )
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

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
