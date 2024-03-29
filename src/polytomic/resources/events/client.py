# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unauthorized_error import UnauthorizedError
from ...types.rest_err_response import RestErrResponse
from ...types.v_2_event_types_envelope import V2EventTypesEnvelope
from ...types.v_2_events_envelope import V2EventsEnvelope

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def api_v_2_get_events(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        starting_after: typing.Optional[dt.datetime] = None,
        ending_before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
    ) -> V2EventsEnvelope:
        """
        Parameters:
            - organization_id: typing.Optional[str].

            - type: typing.Optional[str].

            - starting_after: typing.Optional[dt.datetime].

            - ending_before: typing.Optional[dt.datetime].

            - limit: typing.Optional[int].
        ---
        import datetime

        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.events.api_v_2_get_events(
            organization_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            starting_after=datetime.datetime.fromisoformat(
                "2020-01-01 00:00:00+00:00",
            ),
            ending_before=datetime.datetime.fromisoformat(
                "2020-01-01 00:00:00+00:00",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/events"),
            params=remove_none_from_dict(
                {
                    "organization_id": organization_id,
                    "type": type,
                    "starting_after": serialize_datetime(starting_after) if starting_after is not None else None,
                    "ending_before": serialize_datetime(ending_before) if ending_before is not None else None,
                    "limit": limit,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2EventsEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def api_v_2_get_event_types(self) -> V2EventTypesEnvelope:
        """
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.events.api_v_2_get_event_types()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/events_types"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2EventTypesEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def api_v_2_get_events(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        starting_after: typing.Optional[dt.datetime] = None,
        ending_before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
    ) -> V2EventsEnvelope:
        """
        Parameters:
            - organization_id: typing.Optional[str].

            - type: typing.Optional[str].

            - starting_after: typing.Optional[dt.datetime].

            - ending_before: typing.Optional[dt.datetime].

            - limit: typing.Optional[int].
        ---
        import datetime

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.events.api_v_2_get_events(
            organization_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            starting_after=datetime.datetime.fromisoformat(
                "2020-01-01 00:00:00+00:00",
            ),
            ending_before=datetime.datetime.fromisoformat(
                "2020-01-01 00:00:00+00:00",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/events"),
            params=remove_none_from_dict(
                {
                    "organization_id": organization_id,
                    "type": type,
                    "starting_after": serialize_datetime(starting_after) if starting_after is not None else None,
                    "ending_before": serialize_datetime(ending_before) if ending_before is not None else None,
                    "limit": limit,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2EventsEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def api_v_2_get_event_types(self) -> V2EventTypesEnvelope:
        """
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.events.api_v_2_get_event_types()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/events_types"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2EventTypesEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
