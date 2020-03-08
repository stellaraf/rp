# Standard Library
import sys

try:
    import stackprinter
except ImportError:
    pass
else:
    if sys.stdout.isatty():
        _style = "darkbg2"
    else:
        _style = "plaintext"
    stackprinter.set_excepthook(style=_style)
