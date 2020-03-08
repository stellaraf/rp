# Standard Library
import asyncio
from json import JSONDecodeError
from socket import gaierror

# Third Party
import httpx

# Project
from rp.logger import log
from rp.exceptions import RPError


async def test_reachability(server):
    """Test reachability of a server."""
    if server.url.scheme == "http" and server.url.port is None:
        port = 80
    elif server.url.scheme == "https" and server.url.port is None:
        port = 443
    else:
        port = 443

    try:
        _reader, _writer = await asyncio.open_connection(
            str(server.url.host), int(port)
        )
    except gaierror:
        raise RPError(
            f"{server.url.host}:{port} is unreachable/unresolvable.", status=502
        )
    if _reader or _writer:
        return True
    else:
        return False


class Netbox:
    """Netbox session handler."""

    server = None
    base_url = None
    session = None

    @classmethod
    async def new(cls, server):
        """Create a new session.

        Arguments:
            server {Netbox} -- Netbox configuration object

        Returns:
            {object} -- Netbox session instance
        """
        instance = Netbox()

        await test_reachability(server)

        headers = {"Authorization": f"Token {server.api_key.get_secret_value()}"}

        base_url = str(server.url)

        log.debug(base_url)

        async with httpx.AsyncClient(verify=True, headers=headers) as client:
            try:
                setup = await client.get(base_url + "/api/")

                if setup.status_code != 200:
                    log.error(setup.status_code)
                    log.error(setup.text)
                    status = httpx.status_codes.StatusCode(setup.status_code)
                    status_name = status.name.replace("_", " ")
                    raise RPError(
                        "{msg} - {url}",
                        status=status.value,
                        msg=status_name,
                        url=setup.url,
                    )

            except httpx.HTTPError as http_err:
                raise RPError(str(http_err))

        instance.server = server
        instance.base_url = base_url
        instance.session = httpx.AsyncClient(
            base_url=base_url, verify=True, headers=headers
        )
        log.debug(f"Opened session with {server.url.host}")
        return instance

    async def close(self):
        """Close the Netbox session."""
        await self.session.aclose()

        if not self.session.dispatch.is_closed:
            raise RPError(
                "Unable to close session with {server}",
                status=500,
                server=self.server.url.host,
            )

        log.debug(f"Closed session with {self.server.url.host}")

    async def get(self, endpoint, item=None, params=None):
        """Get data from Netbox using the GET method.

        Arguments:
            endpoint {str} -- Netbox URI endpoint

        Keyword Arguments:
            item {str|int} -- Specific item/id (default: {None})
            params {dict} -- URL filter paramters (default: {None})

        Raises:
            RPError: Raised if status code is not 200.
            RPError: Raised on any http errors.

        Returns:
            {str|dict} -- Try to return structured data, fall back to text.
        """
        if item is not None:
            endpoint = f"{endpoint}/{str(item)}/"

        request_config = {}

        if params is not None:
            request_config.update({"params": params})
        try:
            response = await self.session.get(f"/api{endpoint}", **request_config)

            if response.status_code != 200:
                status = httpx.status_codes.StatusCode(response.status_code)
                status_name = status.name.replace("_", " ")
                raise RPError(
                    "{msg} - {url}",
                    status=status.value,
                    msg=status_name,
                    url=response.url,
                )
        except httpx.HTTPError as http_err:
            raise RPError(str(http_err)) from None
        try:
            return response.json()
        except JSONDecodeError:
            return response.text
