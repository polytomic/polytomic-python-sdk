# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .v_2_identity_function import V2IdentityFunction

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class V2TargetField(pydantic.BaseModel):
    association: typing.Optional[bool]
    createable: typing.Optional[bool]
    description: typing.Optional[str]
    filterable: typing.Optional[bool]
    id: typing.Optional[str]
    identity_functions: typing.Optional[typing.List[V2IdentityFunction]]
    name: typing.Optional[str]
    required: typing.Optional[bool]
    source_type: typing.Optional[str]
    supports_identity: typing.Optional[bool]
    type: typing.Optional[str]
    updateable: typing.Optional[bool]

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
