from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import settings
from common.services.cu_logging import get_logger

_LOGGER = get_logger(__name__)


@contextmanager
def session_scope(expire_on_commit=True, echo=False) -> Session:

    _LOGGER.debug(
        "Creating database session %s", settings.DATABASE_URL
    )  # ! CONNECTION_STRING, which includes password

    engine = create_engine(settings.CONNECTION_STRING, echo=echo)
    session = sessionmaker(bind=engine, expire_on_commit=expire_on_commit)()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
