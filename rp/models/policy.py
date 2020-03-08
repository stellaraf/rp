# Standard Library
from typing import Dict, List, Union, Optional

# Third Party
from pydantic import StrictStr

# Project
from rp.models._common import Flag, RPModel

_policy_from = Optional[
    Dict[
        StrictStr,
        List[
            Union[
                None,
                Dict[StrictStr, Union[None, List[StrictStr], StrictStr]],
                StrictStr,
            ]
        ],
    ]
]

_policy_to = Optional[
    Dict[
        StrictStr,
        List[
            Union[
                None,
                Dict[StrictStr, Union[None, List[StrictStr], StrictStr]],
                StrictStr,
            ]
        ],
    ]
]

_policy_then = Optional[
    Dict[
        StrictStr,
        List[Union[None, StrictStr, Dict[StrictStr, Union[Flag, List[StrictStr]]]]],
    ],
]


class _PolicyBase(RPModel):
    class Config:
        fields = {"policy_from": "from", "policy_to": "to", "policy_then": "then"}


class PolicyTerm(_PolicyBase):
    """JunOS policy/filter term JSON model."""

    name: StrictStr
    policy_from: _policy_from
    policy_to: _policy_to
    policy_then: _policy_then


class Policy(_PolicyBase):
    """JunOS policy/filter JSON model."""

    name: StrictStr
    term: Optional[List[PolicyTerm]]
    policy_from: _policy_from
    policy_to: _policy_to
    policy_then: _policy_then
