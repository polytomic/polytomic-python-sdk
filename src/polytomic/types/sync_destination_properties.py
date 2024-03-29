# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SyncDestinationProperties(pydantic.BaseModel):
    does_not_report_operation_counts: typing.Optional[bool]
    new_target_label: typing.Optional[str]
    optional_target_mappings: typing.Optional[bool]
    primary_metadata_object: typing.Optional[str]
    requires_configuration: typing.Optional[bool]
    supports_field_creation: typing.Optional[bool]
    supports_field_type_selection: typing.Optional[bool]
    supports_target_filters: typing.Optional[bool]
    target_creator: typing.Optional[bool]
    use_field_names_as_labels: typing.Optional[bool]

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
