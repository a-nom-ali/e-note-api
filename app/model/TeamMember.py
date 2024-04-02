from sqlalchemy import create_engine, Table, Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import MetaData
from datetime import datetime


class TeamMember(Table):
    __tablename__ = 'team_members'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    joined_at = Column(TIMESTAMP, default=datetime.utcnow)

    # Relationships
    team = relationship('Team', back_populates='team_members')
    user = relationship('User', back_populates='team_members')
    role = relationship('Role', back_populates='team_members')
