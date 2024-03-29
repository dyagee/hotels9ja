#the schema not used in v2

from pydantic import BaseModel


class HotelBase(BaseModel):
    name: str
    address: str
    price: int

class Hotel(HotelBase):
    hotel_id:str
    state:str
    city:str
    rating:str | None = None
    rated_by: str | None = None
    services:str | None = None
    link: str | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "The Grand Star Hotel",
                "address": "No. 32 Ember Road, Island, Lagos",
                "price": 38000,
                "hotel_id": "90sfkghd96fkgf35jh6h6j091nnb2",
                "state": "Lagos",
                "city": "Apapa",
                "rating": "7.5 Very Good",
                "rated_by": "From 113 Reviews",
                "services": "Bar,Gym,Swimming pool,",
                "link": "https://hotels.ng/hotels-in-lagos/apapa-grand-star-23453",
            }
        }
class HotelAdd(BaseModel):
    hotel_id:str
    name: str
    address: str
    price: int
    state:str
    city:str
    rating:str | None = None
    rated_by: str | None = None
    services:str | None = None
    link: str | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "The Grand Star Hotel",
                "address": "No. 32 Ember Road, Island, Lagos",
                "price": 38000,
                "hotel_id": "90sfkghd96fkgf35jh6h6j091nnb2",
                "state": "Lagos",
                "city": "Apapa",
                "rating": "7.5 Very Good",
                "rated_by": "From 113 Reviews",
                "services": "Bar,Gym,Swimming pool,",
                "link": "https://hotels.ng/hotels-in-lagos/apapa-grand-star-23453",
            }
        }


