import logging.config
import os

from .default import *

try:
    stem_env = os.environ.get("STEM_ENV", "")
    if stem_env == "prod":
        from .prod import *
    else:
        from .local import *


except ImportError:
    pass

logging.config.dictConfig(LOGGING_CONFIG)


def __getattr__(name):
    if name == "ENV":
        return stem_env or "local"

