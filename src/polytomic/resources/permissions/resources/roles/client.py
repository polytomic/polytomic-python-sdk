# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....errors.unauthorized_error import UnauthorizedError
from .....types.rest_err_response import RestErrResponse
from .....types.v_2_role_list_response_envelope import V2RoleListResponseEnvelope
from .....types.v_2_role_response_envelope import V2RoleResponseEnvelope

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RolesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self) -> V2RoleListResponseEnvelope:
        """
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.permissions.roles.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/permissions/roles"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2RoleListResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, name: str, organization_id: typing.Optional[str] = OMIT) -> V2RoleResponseEnvelope:
        """
        Parameters:
            - name: str.

            - organization_id: typing.Optional[str].
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.permissions.roles.create(
            name="Custom",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/permissions/roles"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2RoleResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str) -> V2RoleResponseEnvelope:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.permissions.roles.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/permissions/roles/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2RoleResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str) -> None:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.permissions.roles.delete(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/permissions/roles/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, id: str, *, name: str, organization_id: typing.Optional[str] = OMIT) -> V2RoleResponseEnvelope:
        """
        Parameters:
            - id: str.

            - name: str.

            - organization_id: typing.Optional[str].
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.permissions.roles.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="Custom",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/permissions/roles/{id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2RoleResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRolesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self) -> V2RoleListResponseEnvelope:
        """
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.permissions.roles.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/permissions/roles"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2RoleListResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, name: str, organization_id: typing.Optional[str] = OMIT) -> V2RoleResponseEnvelope:
        """
        Parameters:
            - name: str.

            - organization_id: typing.Optional[str].
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.permissions.roles.create(
            name="Custom",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/permissions/roles"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2RoleResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str) -> V2RoleResponseEnvelope:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.permissions.roles.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/permissions/roles/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2RoleResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str) -> None:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.permissions.roles.delete(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/permissions/roles/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, id: str, *, name: str, organization_id: typing.Optional[str] = OMIT
    ) -> V2RoleResponseEnvelope:
        """
        Parameters:
            - id: str.

            - name: str.

            - organization_id: typing.Optional[str].
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.permissions.roles.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="Custom",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/permissions/roles/{id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2RoleResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
