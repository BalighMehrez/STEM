########################################################################################################################
# Logging Configuration
LOGGING_ROOT = "stem"
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(process)d [%(levelname)s] %(name)s.%(funcName)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        LOGGING_ROOT: {"level": "INFO", "handlers": ["console"], "propagate": False},
        "": {"level": "INFO", "handlers": ["console"], "propagate": False},
    },
    "disable_existing_loggers": False,
}

########################################################################################################################
