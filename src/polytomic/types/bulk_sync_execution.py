# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .bulk_execution_status import BulkExecutionStatus
from .bulk_sync_schema_execution import BulkSyncSchemaExecution

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BulkSyncExecution(pydantic.BaseModel):
    completed_at: typing.Optional[dt.datetime]
    created_at: typing.Optional[dt.datetime]
    id: typing.Optional[str]
    is_resync: typing.Optional[bool]
    is_test: typing.Optional[bool]
    schemas: typing.Optional[typing.List[BulkSyncSchemaExecution]]
    started_at: typing.Optional[dt.datetime]
    status: typing.Optional[BulkExecutionStatus]
    type: typing.Optional[str]

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