import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import *


Base = declarative_base()
 

 
class Events(Base):
    __tablename__ = 'create_events'
    id = Column(Integer, primary_key=True)
    event_name = Column(String(250), nullable=False)
    event_start_date=Column(String(250), nullable=False)
    event_end_date = Column(String(250), nullable=False)
    event_venue = Column(String(250), nullable=False)
    tickets = relationship('Tickets', backref='create_events',
                                lazy='dynamic')

class Tickets(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('create_events.id'))
    ticket_status = Column(String(250), default='valid')
    
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///tickets.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)