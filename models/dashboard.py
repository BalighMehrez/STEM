from sqlalchemy import Column, Integer, String

from models.constants import Base


class Dashboard(Base):
    __tablename__ = "dashboard"
    connection_type = Column(Integer, nullable=False)
    connection_string = Column(String(), nullable=False)
    query = Column(String(), nullable=False)
    header = Column(String(), nullable=False)
