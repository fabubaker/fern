import typing

import pydantic


class LangServerRequest(pydantic.BaseModel):
    request: typing.Any

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True
