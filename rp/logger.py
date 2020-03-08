# Standard Library
import sys

# Third Party
from loguru import logger as _loguru_logger

LOG_FMT = (
    "<lvl><b>[{level}]</b> {time:YYYYMMDD} {time:HH:mm:ss} <lw>|</lw> {name}<lw>:</lw>"
    "<b>{line}</b> <lw>|</lw> {function}</lvl> <lvl><b>→</b></lvl> {message}"
)


LOG_LEVELS = [
    {"name": "DEBUG", "no": 10, "color": "<c>"},
    {"name": "INFO", "no": 20, "color": "<le>"},
    {"name": "SUCCESS", "no": 25, "color": "<g>"},
    {"name": "WARNING", "no": 30, "color": "<y>"},
    {"name": "ERROR", "no": 40, "color": "<y>"},
    {"name": "CRITICAL", "no": 50, "color": "<r>"},
]

LOG_HANDLER = {"sink": sys.stdout, "format": LOG_FMT, "level": "DEBUG"}


def _logger():
    _loguru_logger.remove()
    _loguru_logger.configure(handlers=[LOG_HANDLER], levels=LOG_LEVELS)
    return _loguru_logger


log = _logger()
