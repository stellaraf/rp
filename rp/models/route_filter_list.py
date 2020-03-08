# Standard Library
from typing import List, Union, Optional
from ipaddress import IPv4Network, IPv6Network

# Third Party
from pydantic import StrictStr

# Project
from rp.models._common import Flag, RPModel


class RouteFilterEntry(RPModel):
    """JunOS route-filter-list item JSON model."""

    address: Union[IPv4Network, IPv6Network]
    longer: Flag
    orlonger: Flag
    exact: Flag
    prefix_length_range: Optional[StrictStr]
    through: Optional[StrictStr]
    upto: Optional[StrictStr]

    class Config:
        """Pydantic config overrides."""

        fields = {"prefix_length_range": "prefix-length-range"}


class RouteFilterList(RPModel):
    """JunOS route-filter-list JSON model."""

    name: StrictStr
    rf_list: List[RouteFilterEntry]
