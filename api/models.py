#for now using a localized model
#with time the generalized api model will be 
#set up seperately

from sqlalchemy import  Column,Integer, String,Text,Float

from database import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(String,unique=True)
    name = Column(String, index=True)
    city = Column(String)
    state = Column(String)
    price = Column(Integer)
    rating = Column(Float)
    rated_by = Column(String)
    services = Column(String)
    address = Column(Text)
    link = Column(String)