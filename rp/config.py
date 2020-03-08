# Standard Library
from pathlib import Path

# Third Party
import yaml

# Project
from rp.models.config import Params

CONFIG_FILE = Path(__file__).parent / "config.yaml"


def _get_config():
    with CONFIG_FILE.open("r") as cf:
        cf_yaml = yaml.safe_load(cf.read()) or {}

    valid_config = Params(**cf_yaml)
    return valid_config


params = _get_config()
