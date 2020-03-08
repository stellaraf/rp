# Third Party
from pydantic import StrictStr

# Project
from rp.models._common import RPModel


class ASPath(RPModel):
    """JunOS as-path JSON model."""

    name: StrictStr
    path: StrictStr
