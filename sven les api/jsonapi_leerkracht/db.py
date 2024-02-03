from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the database engine
engine = create_engine("postgresql://car_master:cars_master@localhost:5432/cars", echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define the Car models
class EV(Base):
    __tablename__ = "evs"
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    range = Column(Integer)
    year = Column(Integer)
    price = Column(Integer)

class ICE(Base):
    __tablename__ = "ices"
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    fueltype = Column(String)
    mpg = Column(Integer)
    year = Column(Integer)
    price = Column(Integer)

# Create the database tables
Base.metadata.create_all(engine)