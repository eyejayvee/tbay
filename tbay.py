# Import modules to create the engine, session and base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Import the modules for the model
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float

# Instantiate the engine, session and base
engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Create the Item model and table
class Item(Base):
  __tablename__ = "items"
  
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  description = Column(String)
  start_time = Column(DateTime, default=datetime.utcnow)

# Create the User model and table
class User(Base):
  __tablename__ = "user"
  
  id = Column(Integer, primary_key=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)
form 
# Create the Bid model and table
class Bid(Base):
  __tablename__ = "bid"
  
  id = Column(Integer, primary_key=True)
  price = Column(Float, nullable=False)
  
Base.metadata.create_all(engine)