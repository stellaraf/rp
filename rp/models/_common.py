# Standard Library
from typing import List, TypeVar, Optional
from ipaddress import IPv4Network, IPv6Network

# Third Party
from pydantic import BaseModel


class RPModel(BaseModel):
    """Route Policy base model for common settings & functions."""

    class Config:
        """Pydantic config overrides."""

        extra = "forbid"
        validate_assignment = True

    def export_json(self, *args, **kwargs):
        """Return instance as JSON.

        Returns:
            {str} -- Stringified JSON.
        """
        return self.json(by_alias=True, exclude_unset=True, *args, **kwargs)

    def export_dict(self, *args, **kwargs):
        """Return instance as dictionary.

        Returns:
            {dict} -- Python dictionary.
        """
        return self.dict(by_alias=True, exclude_unset=True, *args, **kwargs)


Flag = TypeVar(Optional[List[None]])

Network = TypeVar(IPv4Network, IPv6Network)
