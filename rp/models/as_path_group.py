# Standard Library
from typing import List

# Third Party
from pydantic import StrictStr

# Project
from rp.models._common import RPModel
from rp.models.as_path import ASPath


class ASPathGroup(RPModel):
    """JunOS as-path-group JSON model."""

    name: StrictStr
    members: List[ASPath]
