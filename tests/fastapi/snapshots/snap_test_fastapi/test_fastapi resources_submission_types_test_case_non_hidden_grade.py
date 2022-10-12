# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.variable_value import VariableValue
from .exception_v_2 import ExceptionV2


class TestCaseNonHiddenGrade(pydantic.BaseModel):
    passed: bool
    actual_result: typing.Optional[VariableValue] = pydantic.Field(alias="actualResult")
    exception: typing.Optional[ExceptionV2]
    stdout: str

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseNonHiddenGrade.Validators.field("passed")
            def validate_passed(v: bool, values: TestCaseNonHiddenGrade.Partial) -> bool:
                ...

            @TestCaseNonHiddenGrade.Validators.field("actual_result")
            def validate_actual_result(v: typing.Optional[VariableValue], values: TestCaseNonHiddenGrade.Partial) -> typing.Optional[VariableValue]:
                ...

            @TestCaseNonHiddenGrade.Validators.field("exception")
            def validate_exception(v: typing.Optional[ExceptionV2], values: TestCaseNonHiddenGrade.Partial) -> typing.Optional[ExceptionV2]:
                ...

            @TestCaseNonHiddenGrade.Validators.field("stdout")
            def validate_stdout(v: str, values: TestCaseNonHiddenGrade.Partial) -> str:
                ...
        """

        _passed_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators.PassedValidator]] = []
        _actual_result_validators: typing.ClassVar[
            typing.List[TestCaseNonHiddenGrade.Validators.ActualResultValidator]
        ] = []
        _exception_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators.ExceptionValidator]] = []
        _stdout_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators.StdoutValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["passed"]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.PassedValidator], TestCaseNonHiddenGrade.Validators.PassedValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["actual_result"]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.ActualResultValidator],
            TestCaseNonHiddenGrade.Validators.ActualResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception"]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.ExceptionValidator], TestCaseNonHiddenGrade.Validators.ExceptionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.StdoutValidator], TestCaseNonHiddenGrade.Validators.StdoutValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "passed":
                    cls._passed_validators.append(validator)
                if field_name == "actual_result":
                    cls._actual_result_validators.append(validator)
                if field_name == "exception":
                    cls._exception_validators.append(validator)
                if field_name == "stdout":
                    cls._stdout_validators.append(validator)
                return validator

            return decorator

        class PassedValidator(typing_extensions.Protocol):
            def __call__(self, v: bool, *, values: TestCaseNonHiddenGrade.Partial) -> bool:
                ...

        class ActualResultValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[VariableValue], *, values: TestCaseNonHiddenGrade.Partial
            ) -> typing.Optional[VariableValue]:
                ...

        class ExceptionValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[ExceptionV2], *, values: TestCaseNonHiddenGrade.Partial
            ) -> typing.Optional[ExceptionV2]:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: TestCaseNonHiddenGrade.Partial) -> str:
                ...

    @pydantic.validator("passed")
    def _validate_passed(cls, v: bool, values: TestCaseNonHiddenGrade.Partial) -> bool:
        for validator in TestCaseNonHiddenGrade.Validators._passed_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("actual_result")
    def _validate_actual_result(
        cls, v: typing.Optional[VariableValue], values: TestCaseNonHiddenGrade.Partial
    ) -> typing.Optional[VariableValue]:
        for validator in TestCaseNonHiddenGrade.Validators._actual_result_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("exception")
    def _validate_exception(
        cls, v: typing.Optional[ExceptionV2], values: TestCaseNonHiddenGrade.Partial
    ) -> typing.Optional[ExceptionV2]:
        for validator in TestCaseNonHiddenGrade.Validators._exception_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("stdout")
    def _validate_stdout(cls, v: str, values: TestCaseNonHiddenGrade.Partial) -> str:
        for validator in TestCaseNonHiddenGrade.Validators._stdout_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing.TypedDict):
        passed: typing_extensions.NotRequired[bool]
        actual_result: typing_extensions.NotRequired[typing.Optional[VariableValue]]
        exception: typing_extensions.NotRequired[typing.Optional[ExceptionV2]]
        stdout: typing_extensions.NotRequired[str]

    class Config:
        frozen = True
        allow_population_by_field_name = True
