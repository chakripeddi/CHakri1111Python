"""
Database models and operations
"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    preferences = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class CommandHistory(Base):
    __tablename__ = 'command_history'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    command = Column(String)
    execution_time = Column(DateTime, default=datetime.utcnow)
    status = Column(String)

def init_db():
    from config.settings import DATABASE_URL
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()