# Standard Library
from typing import List

# Third Party
from pydantic import StrictStr

# Project
from rp.models._common import Flag, RPModel


class Community(RPModel):
    """JunOS community JSON model."""

    name: StrictStr
    members: List[StrictStr]
    invert_match: Flag

    class Config:
        """Pydantic config overrides."""

        fields = {"invert_match": "invert-match"}
