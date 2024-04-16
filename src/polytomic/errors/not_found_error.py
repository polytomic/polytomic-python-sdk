# This file was auto-generated from our API Definition.

from ..core.api_error import ApiError as core_api_error_ApiError
from ..types.api_error import ApiError as types_api_error_ApiError


class NotFoundError(core_api_error_ApiError):
    def __init__(self, body: types_api_error_ApiError):
        super().__init__(status_code=404, body=body)
