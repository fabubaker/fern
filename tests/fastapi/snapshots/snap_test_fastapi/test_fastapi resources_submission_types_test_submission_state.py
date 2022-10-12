# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.problem_id import ProblemId
from ...commons.types.test_case import TestCase
from .test_submission_status import TestSubmissionStatus


class TestSubmissionState(pydantic.BaseModel):
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    default_test_cases: typing.List[TestCase] = pydantic.Field(alias="defaultTestCases")
    custom_test_cases: typing.List[TestCase] = pydantic.Field(alias="customTestCases")
    status: TestSubmissionStatus

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestSubmissionState.Validators.field("problem_id")
            def validate_problem_id(v: ProblemId, values: TestSubmissionState.Partial) -> ProblemId:
                ...

            @TestSubmissionState.Validators.field("default_test_cases")
            def validate_default_test_cases(v: typing.List[TestCase], values: TestSubmissionState.Partial) -> typing.List[TestCase]:
                ...

            @TestSubmissionState.Validators.field("custom_test_cases")
            def validate_custom_test_cases(v: typing.List[TestCase], values: TestSubmissionState.Partial) -> typing.List[TestCase]:
                ...

            @TestSubmissionState.Validators.field("status")
            def validate_status(v: TestSubmissionStatus, values: TestSubmissionState.Partial) -> TestSubmissionStatus:
                ...
        """

        _problem_id_validators: typing.ClassVar[typing.List[TestSubmissionState.Validators.ProblemIdValidator]] = []
        _default_test_cases_validators: typing.ClassVar[
            typing.List[TestSubmissionState.Validators.DefaultTestCasesValidator]
        ] = []
        _custom_test_cases_validators: typing.ClassVar[
            typing.List[TestSubmissionState.Validators.CustomTestCasesValidator]
        ] = []
        _status_validators: typing.ClassVar[typing.List[TestSubmissionState.Validators.StatusValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"]
        ) -> typing.Callable[
            [TestSubmissionState.Validators.ProblemIdValidator], TestSubmissionState.Validators.ProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["default_test_cases"]
        ) -> typing.Callable[
            [TestSubmissionState.Validators.DefaultTestCasesValidator],
            TestSubmissionState.Validators.DefaultTestCasesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_test_cases"]
        ) -> typing.Callable[
            [TestSubmissionState.Validators.CustomTestCasesValidator],
            TestSubmissionState.Validators.CustomTestCasesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"]
        ) -> typing.Callable[
            [TestSubmissionState.Validators.StatusValidator], TestSubmissionState.Validators.StatusValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_id":
                    cls._problem_id_validators.append(validator)
                if field_name == "default_test_cases":
                    cls._default_test_cases_validators.append(validator)
                if field_name == "custom_test_cases":
                    cls._custom_test_cases_validators.append(validator)
                if field_name == "status":
                    cls._status_validators.append(validator)
                return validator

            return decorator

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, v: ProblemId, *, values: TestSubmissionState.Partial) -> ProblemId:
                ...

        class DefaultTestCasesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[TestCase], *, values: TestSubmissionState.Partial
            ) -> typing.List[TestCase]:
                ...

        class CustomTestCasesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[TestCase], *, values: TestSubmissionState.Partial
            ) -> typing.List[TestCase]:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(self, v: TestSubmissionStatus, *, values: TestSubmissionState.Partial) -> TestSubmissionStatus:
                ...

    @pydantic.validator("problem_id")
    def _validate_problem_id(cls, v: ProblemId, values: TestSubmissionState.Partial) -> ProblemId:
        for validator in TestSubmissionState.Validators._problem_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("default_test_cases")
    def _validate_default_test_cases(
        cls, v: typing.List[TestCase], values: TestSubmissionState.Partial
    ) -> typing.List[TestCase]:
        for validator in TestSubmissionState.Validators._default_test_cases_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("custom_test_cases")
    def _validate_custom_test_cases(
        cls, v: typing.List[TestCase], values: TestSubmissionState.Partial
    ) -> typing.List[TestCase]:
        for validator in TestSubmissionState.Validators._custom_test_cases_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("status")
    def _validate_status(cls, v: TestSubmissionStatus, values: TestSubmissionState.Partial) -> TestSubmissionStatus:
        for validator in TestSubmissionState.Validators._status_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing.TypedDict):
        problem_id: typing_extensions.NotRequired[ProblemId]
        default_test_cases: typing_extensions.NotRequired[typing.List[TestCase]]
        custom_test_cases: typing_extensions.NotRequired[typing.List[TestCase]]
        status: typing_extensions.NotRequired[TestSubmissionStatus]

    class Config:
        frozen = True
        allow_population_by_field_name = True
