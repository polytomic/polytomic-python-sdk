# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class V2GetIdentityResponseSchema(pydantic.BaseModel):
    email: typing.Optional[str]
    id: typing.Optional[str]
    is_organization: typing.Optional[bool]
    is_partner: typing.Optional[bool]
    is_system: typing.Optional[bool]
    is_user: typing.Optional[bool]
    organization_id: typing.Optional[str]
    organization_name: typing.Optional[str]
    role: typing.Optional[str]

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
