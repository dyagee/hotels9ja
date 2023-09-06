from models import ErrorResponseModel
from database import col


#load all hotels by names
def showHotels(skip:int,limit:int ):
   return col.find({'_id':False}).skip(skip).limit(limit).sort({'name':1}) 
   #return db.query(Hotel).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()

def showByID(hotel_id:str):
    HID =str(hotel_id)
    return col.findOne({'hotel_id': HID}, {'_id': False})
    #return db.query(Hotel).filter(Hotel.hotel_id == HID).first()

   
def showByState(State:str,skip:int,limit:int):
    State =State.lower()
    return col.find({'state': State}, {'_id': False}).skip(skip).limit(limit).sort({'name':1})
    #return db.query(Hotel).filter_by(state=State).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()
   
def showByCity(City:str,skip:int,limit:int):
    City= City.strip().lower()
    return col.find({'city': City}, {'_id': False}).skip(skip).limit(limit).sort({'name':1})
    #return db.query(Hotel).filter(Hotel.city == City).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()
   

def showStrict(State:str,City:str,skip:int,limit:int):
    State = State.lower()
    City=City.lower()
    return col.find({'state': State, 'city':City}, {'_id': False}).skip(skip).limit(limit).sort({'name':1})
    #return db.query(Hotel).filter(Hotel.state==State,Hotel.city==City).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()
   

def Cheap(skip:int,limit:int):
    hotels =[]
    #checks = db.query(Hotel).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()
    checks = col.find({'_id':False}).skip(skip).limit(limit).sort({'name':1}) 
    for hotel in checks:
        p = int(hotel['price'])
        if p <= 10000:
            hotels.append(hotel)
    return hotels


   
def Moderate(skip:int,limit:int):
    Moderatehotels =[]
    #checks = db.query(Hotel).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()
    checks = col.find({'_id':False}).skip(skip).limit(limit).sort({'name':1})
    for hotel in checks:
        p = int(hotel['price'])
        if (p>10000 and p<=20000):
            Moderatehotels.append(hotel)
    return Moderatehotels
def Exotic(skip:int,limit:int):
    Exotichotels =[]
    #checks = db.query(Hotel).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()
    checks = col.find({'_id':False}).skip(skip).limit(limit).sort({'name':1})
    for hotel in checks:
        p = int(hotel['price'])
        if (p>20000):
            Exotichotels.append(hotel)
    return Exotichotels

def CityPrice(City:str,Price:int,skip:int,limit:int):
    City=City.strip().lower()
    pp = int(Price)
    Cityhotels =[]

    #checks_ = db.query(Hotel).filter_by(city=City).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()
    checks_ = col.find({'city': City}, {'_id': False}).skip(skip).limit(limit).sort({'name':1})
    if checks_ is not None:
        for hotel in checks_:
            p = int(hotel['price'])
            if p <=pp:
                Cityhotels.append(hotel)
        return Cityhotels


def StatePrice(State:str,Price:int,skip:int,limit:int):
    State=State.strip().lower()
    sp = int(Price)
    Statehotels = []
    #checks = db.query(Hotel).filter(Hotel.state==State).order_by(Hotel.name.asc()).offset(skip).limit(limit).all()
    checks = col.find({'state': State}, {'_id': False}).skip(skip).limit(limit).sort({'name':1})
    if checks is not None:
        for hotel in checks:
            p = int(hotel['price'])
            if p <= sp:
                Statehotels.append(hotel)
        return Statehotels
   

