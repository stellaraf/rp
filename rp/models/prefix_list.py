# Standard Library
from typing import List

# Third Party
from pydantic import StrictStr

# Project
from rp.models._common import Network, RPModel


class PrefixListItem(RPModel):
    """JunOS prefix-list-item JSON model."""

    name: Network


class PrefixList(RPModel):
    """JunOS prefix-list JSON model."""

    name: StrictStr
    prefix_list_item: List[PrefixListItem]

    class Config:
        """Pydantic config overrides."""

        fields = {"prefix_list_item": "prefix-list-item"}
