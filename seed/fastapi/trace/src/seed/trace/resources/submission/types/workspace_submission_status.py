# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

from .error_info import ErrorInfo
from .running_submission_state import RunningSubmissionState
from .workspace_run_details import WorkspaceRunDetails

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def stopped(self) -> WorkspaceSubmissionStatus:
        return WorkspaceSubmissionStatus(__root__=_WorkspaceSubmissionStatus.Stopped(type="stopped"))

    def errored(self, value: ErrorInfo) -> WorkspaceSubmissionStatus:
        return WorkspaceSubmissionStatus(__root__=_WorkspaceSubmissionStatus.Errored(type="errored", value=value))

    def running(self, value: RunningSubmissionState) -> WorkspaceSubmissionStatus:
        return WorkspaceSubmissionStatus(__root__=_WorkspaceSubmissionStatus.Running(type="running", value=value))

    def ran(self, value: WorkspaceRunDetails) -> WorkspaceSubmissionStatus:
        return WorkspaceSubmissionStatus(
            __root__=_WorkspaceSubmissionStatus.Ran(**value.dict(exclude_unset=True), type="ran")
        )

    def traced(self, value: WorkspaceRunDetails) -> WorkspaceSubmissionStatus:
        return WorkspaceSubmissionStatus(
            __root__=_WorkspaceSubmissionStatus.Traced(**value.dict(exclude_unset=True), type="traced")
        )


class WorkspaceSubmissionStatus(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _WorkspaceSubmissionStatus.Stopped,
        _WorkspaceSubmissionStatus.Errored,
        _WorkspaceSubmissionStatus.Running,
        _WorkspaceSubmissionStatus.Ran,
        _WorkspaceSubmissionStatus.Traced,
    ]:
        return self.__root__

    def visit(
        self,
        stopped: typing.Callable[[], T_Result],
        errored: typing.Callable[[ErrorInfo], T_Result],
        running: typing.Callable[[RunningSubmissionState], T_Result],
        ran: typing.Callable[[WorkspaceRunDetails], T_Result],
        traced: typing.Callable[[WorkspaceRunDetails], T_Result],
    ) -> T_Result:
        if self.__root__.type == "stopped":
            return stopped()
        if self.__root__.type == "errored":
            return errored(self.__root__.value)
        if self.__root__.type == "running":
            return running(self.__root__.value)
        if self.__root__.type == "ran":
            return ran(WorkspaceRunDetails(**self.__root__.dict(exclude_unset=True, exclude={"type"})))
        if self.__root__.type == "traced":
            return traced(WorkspaceRunDetails(**self.__root__.dict(exclude_unset=True, exclude={"type"})))

    __root__: typing_extensions.Annotated[
        typing.Union[
            _WorkspaceSubmissionStatus.Stopped,
            _WorkspaceSubmissionStatus.Errored,
            _WorkspaceSubmissionStatus.Running,
            _WorkspaceSubmissionStatus.Ran,
            _WorkspaceSubmissionStatus.Traced,
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


class _WorkspaceSubmissionStatus:
    class Stopped(pydantic.BaseModel):
        type: typing_extensions.Literal["stopped"]

    class Errored(pydantic.BaseModel):
        type: typing_extensions.Literal["errored"]
        value: ErrorInfo

    class Running(pydantic.BaseModel):
        type: typing_extensions.Literal["running"]
        value: RunningSubmissionState

    class Ran(WorkspaceRunDetails):
        type: typing_extensions.Literal["ran"]

        class Config:
            allow_population_by_field_name = True

    class Traced(WorkspaceRunDetails):
        type: typing_extensions.Literal["traced"]

        class Config:
            allow_population_by_field_name = True


WorkspaceSubmissionStatus.update_forward_refs()
