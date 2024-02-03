# from sqlalchemy import create_engine,column,Integer,String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresql://cars_master:cars_master@localhost:5432/cars', echo=True)

# session=sessionmaker(bind=engine)

# base=declarative_base()

# class ev(base):
#     __tablename__="ev"
#     id=column(Integer,primary_key=True)
#     brand=column(String)
#     model=column(String)
#     range=column(Integer)
#     year=column(Integer)
#     price=column(Integer)

# class ice(base):
#     __tablename__="ice"
#     id=column(Integer,primary_key=True)
#     brand=column(String)
#     model=column(String)
#     fuelType=column(String)
#     mpg=column(Integer)
#     year=column(Integer)
#     price=column(Integer)

# base.metadata.create_all(engine)

