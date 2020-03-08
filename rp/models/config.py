# Standard Library
from typing import List

# Third Party
from pydantic import HttpUrl, BaseModel, SecretStr


class Netbox(BaseModel):
    """Netbox parameters."""

    url: HttpUrl
    api_key: SecretStr


class Params(BaseModel):
    """App-wide parameters."""

    netbox: Netbox
    sites: List
