import logging

import settings

_root_logger = logging.getLogger(settings.LOGGING_ROOT)


def get_logger(name: str) -> logging.Logger:
    logger = _root_logger.getChild(name)
    return logger
