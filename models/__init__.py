from sqlalchemy import Column, Integer, String, Float, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql

engine = create_engine("mysql+pymysql://root@localhost/factura2345?charset=utf8mb4") 

connection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

Base.metadata.bind = engine

