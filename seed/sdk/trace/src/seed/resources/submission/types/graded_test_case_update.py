# This file was auto-generated by Fern from our API Definition.

from .test_case_grade import TestCaseGrade

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...v_2.resources.problem.types.test_case_id import TestCaseId


class GradedTestCaseUpdate(pydantic.BaseModel):
    test_case_id: TestCaseId = pydantic.Field(alias="testCaseId")
    grade: TestCaseGrade

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
