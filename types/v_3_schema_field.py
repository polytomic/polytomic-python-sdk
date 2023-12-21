# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .schema_association import SchemaAssociation
from .v_3_pick_value import V3PickValue

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class V3SchemaField(pydantic.BaseModel):
    association: typing.Optional[SchemaAssociation]
    id: typing.Optional[str]
    name: typing.Optional[str]
    remote_type: typing.Optional[str]
    type: typing.Optional[str]
    values: typing.Optional[typing.List[V3PickValue]]

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
