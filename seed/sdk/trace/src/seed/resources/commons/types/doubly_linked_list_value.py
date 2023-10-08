# This file was auto-generated by Fern from our API Definition.

import typing

from ....core.datetime_utils import serialize_datetime
from .node_id import NodeId

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt

from .doubly_linked_list_node_value import DoublyLinkedListNodeValue


class DoublyLinkedListValue(pydantic.BaseModel):
    head: typing.Optional[NodeId]
    nodes: typing.Dict[NodeId, DoublyLinkedListNodeValue]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
