# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .object_value import ObjectValue
from .primitive_value import PrimitiveValue

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ContainerValue_List(pydantic.BaseModel):
    type: typing.Literal["list"] = "list"
    value: typing.List[FieldValue]

    class Config:
        frozen = True
        smart_union = True


class ContainerValue_Optional(pydantic.BaseModel):
    type: typing.Literal["optional"] = "optional"
    value: typing.Optional[FieldValue]

    class Config:
        frozen = True
        smart_union = True


ContainerValue = typing.Union[ContainerValue_List, ContainerValue_Optional]
from .field_value import FieldValue  # noqa: E402

ContainerValue_List.update_forward_refs(ContainerValue=ContainerValue, FieldValue=FieldValue)
ContainerValue_Optional.update_forward_refs(ContainerValue=ContainerValue, FieldValue=FieldValue)