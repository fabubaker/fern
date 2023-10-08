# This file was auto-generated by Fern from our API Definition.

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .node_id import NodeId
from .singly_linked_list_value import SinglyLinkedListValue


class SinglyLinkedListNodeAndListValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_list: SinglyLinkedListValue = pydantic.Field(alias="fullList")

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
