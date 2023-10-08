# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .test_case_grade import TestCaseGrade
from .test_case_result_with_stdout import TestCaseResultWithStdout
from .traced_test_case import TracedTestCase

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt

import typing_extensions

from ....core.datetime_utils import serialize_datetime

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def graded(self, value: TestCaseResultWithStdout) -> SubmissionStatusForTestCase:
        return SubmissionStatusForTestCase(
            __root__=_SubmissionStatusForTestCase.Graded(**value.dict(exclude_unset=True), type="graded")
        )

    def graded_v_2(self, value: TestCaseGrade) -> SubmissionStatusForTestCase:
        return SubmissionStatusForTestCase(__root__=_SubmissionStatusForTestCase.GradedV2(type="gradedV2", value=value))

    def traced(self, value: TracedTestCase) -> SubmissionStatusForTestCase:
        return SubmissionStatusForTestCase(
            __root__=_SubmissionStatusForTestCase.Traced(**value.dict(exclude_unset=True), type="traced")
        )


class SubmissionStatusForTestCase(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _SubmissionStatusForTestCase.Graded, _SubmissionStatusForTestCase.GradedV2, _SubmissionStatusForTestCase.Traced
    ]:
        return self.__root__

    def visit(
        self,
        graded: typing.Callable[[TestCaseResultWithStdout], T_Result],
        graded_v_2: typing.Callable[[TestCaseGrade], T_Result],
        traced: typing.Callable[[TracedTestCase], T_Result],
    ) -> T_Result:
        if self.__root__.type == "graded":
            return graded(TestCaseResultWithStdout(**self.__root__.dict(exclude_unset=True, exclude={"type"})))
        if self.__root__.type == "gradedV2":
            return graded_v_2(self.__root__.value)
        if self.__root__.type == "traced":
            return traced(TracedTestCase(**self.__root__.dict(exclude_unset=True, exclude={"type"})))

    __root__: typing_extensions.Annotated[
        typing.Union[
            _SubmissionStatusForTestCase.Graded,
            _SubmissionStatusForTestCase.GradedV2,
            _SubmissionStatusForTestCase.Traced,
        ],
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


class _SubmissionStatusForTestCase:
    class Graded(TestCaseResultWithStdout):
        type: typing_extensions.Literal["graded"]

        class Config:
            allow_population_by_field_name = True

    class GradedV2(pydantic.BaseModel):
        type: typing_extensions.Literal["gradedV2"]
        value: TestCaseGrade

    class Traced(TracedTestCase):
        type: typing_extensions.Literal["traced"]

        class Config:
            allow_population_by_field_name = True


SubmissionStatusForTestCase.update_forward_refs()
