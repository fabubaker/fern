# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

from .parameter_id import ParameterId

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt
import typing

import typing_extensions

from ........core.datetime_utils import serialize_datetime

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def html(self, value: str) -> TestCaseImplementationDescriptionBoard:
        return TestCaseImplementationDescriptionBoard(
            __root__=_TestCaseImplementationDescriptionBoard.Html(type="html", value=value)
        )

    def param_id(self, value: ParameterId) -> TestCaseImplementationDescriptionBoard:
        return TestCaseImplementationDescriptionBoard(
            __root__=_TestCaseImplementationDescriptionBoard.ParamId(type="paramId", value=value)
        )


class TestCaseImplementationDescriptionBoard(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId]:
        return self.__root__

    def visit(
        self, html: typing.Callable[[str], T_Result], param_id: typing.Callable[[ParameterId], T_Result]
    ) -> T_Result:
        if self.__root__.type == "html":
            return html(self.__root__.value)
        if self.__root__.type == "paramId":
            return param_id(self.__root__.value)

    __root__: typing_extensions.Annotated[
        typing.Union[_TestCaseImplementationDescriptionBoard.Html, _TestCaseImplementationDescriptionBoard.ParamId],
        pydantic.Field(discriminator="type"),
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _TestCaseImplementationDescriptionBoard:
    class Html(pydantic.BaseModel):
        type: typing_extensions.Literal["html"]
        value: str

    class ParamId(pydantic.BaseModel):
        type: typing_extensions.Literal["paramId"]
        value: ParameterId


TestCaseImplementationDescriptionBoard.update_forward_refs()
