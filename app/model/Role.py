from sqlalchemy import create_engine, Table, Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import MetaData
from datetime import datetime


class Role(Table):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    permissions = Column(Text)  # This could be a JSON field

    # Relationships
    team_members = relationship('TeamMember', back_populates='role')
