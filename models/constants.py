from enum import IntEnum

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base


class ConnectionTypes(IntEnum):
    CSV = 0
    POSTGRES = 1


class CellTypes(IntEnum):
    HEADING = 0  # Text Heading
    DDL = 1  # Dropdown list
    TABLE = 2  # ready to be converted to processed table
    GRAPH = 3  # had been converted to processed table


NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
Base = declarative_base(metadata=MetaData(naming_convention=NAMING_CONVENTION))
