# Third Party
import ujson as _json

# Project
from rp.logger import log


class RPError(Exception):
    """Generic Exception for Route Policy.

    Arguments:
        message {str} -- Error message with str.format() variables
        status {int} -- HTTP Status Code
    """

    def __init__(self, message="", status=500, **kwargs):
        """Create RPError exception.

        Keyword Arguments:
            message {str} -- Error message (default: {""})
            status {int} -- HTTP status code (default: {500})
        """
        self.message = message.format(**kwargs)
        self.status = status
        self.obj = {"error": {"status": self.status, "message": self.message}}
        log.critical(f"{self.status}: {self.message}")

    def __str__(self):
        """Get error message as a string.

        Returns:
            str -- Formatted error message
        """
        return self.message

    def dict(self):
        """Get error as a Python dictionary.

        Returns:
            dict -- {"Error": {"status": [HTTP Status Code], "message": [Formatted error message]}}
        """
        return self.obj

    def json(self):
        """Get error as a stringified JSON object.

        Returns:
            str -- '{"Error": {"status": [HTTP Status Code], "message": [Formatted error message]}}'
        """
        return _json.dumps(self.obj)
