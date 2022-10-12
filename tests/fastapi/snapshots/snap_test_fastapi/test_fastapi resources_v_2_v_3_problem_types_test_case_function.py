# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_with_actual_result_implementation import TestCaseWithActualResultImplementation
from .void_function_definition import VoidFunctionDefinition

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def with_actual_result(self, value: TestCaseWithActualResultImplementation) -> TestCaseFunction:
        return TestCaseFunction(__root__=_TestCaseFunction.WithActualResult(**dict(value), type="withActualResult"))

    def custom(self, value: VoidFunctionDefinition) -> TestCaseFunction:
        return TestCaseFunction(__root__=_TestCaseFunction.Custom(**dict(value), type="custom"))


class TestCaseFunction(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom]:
        return self.__root__

    def visit(
        self,
        with_actual_result: typing.Callable[[TestCaseWithActualResultImplementation], T_Result],
        custom: typing.Callable[[VoidFunctionDefinition], T_Result],
    ) -> T_Result:
        if self.__root__.type == "withActualResult":
            return with_actual_result(self.__root__)
        if self.__root__.type == "custom":
            return custom(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom], pydantic.Field(discriminator="type")
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseFunction.Validators.validate
            def validate(value: typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom]) -> typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom]],
                    typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom]],
                typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_TestCaseFunction.WithActualResult, _TestCaseFunction.Custom], values.get("__root__")
        )
        for validator in TestCaseFunction.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True


class _TestCaseFunction:
    class WithActualResult(TestCaseWithActualResultImplementation):
        type: typing_extensions.Literal["withActualResult"]

        class Config:
            frozen = True

    class Custom(VoidFunctionDefinition):
        type: typing_extensions.Literal["custom"]

        class Config:
            frozen = True


TestCaseFunction.update_forward_refs()
