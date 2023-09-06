from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from routes import*
#from  models import Base
from schemas import Hotel
from database import RANDOM_N, MONGODB_URI

app = FastAPI()
#this is just for debuging 
@app.get("/another")
def another():
    message = {'message':'This is another route test',
               'key':RANDOM_N}
    return message
@app.get("/uri")
def uri():
    message = {'message':'This is the mongodb uri',
               'uri':MONGODB_URI}
    return message



@app.get("/")
def docs_redirect():
    return RedirectResponse(url='/docs')
    
@app.get("/hotels/", response_model=list[Hotel])
def all_hotels(skip: int = 0, limit: int = 100):
    hotels = showHotels( skip=skip, limit=limit)
    return hotels

@app.get("/hotel/{id}/", response_model=Hotel)
def hotel_by_id(id:str):
    hotels = showByID(hotel_id=id)
    return hotels

@app.get("/hotels/{State}/", response_model=list[Hotel])
def show_by_State(State:str,skip: int = 0, limit: int = 50):
    hotels = showByState(State=State,skip=skip,limit=limit)
    if hotels is None:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/hotels/{City}/all/", response_model=list[Hotel])
def show_by_City(City:str,skip: int = 0, limit: int = 50):
    hotels = showByCity(City=City,skip=skip,limit=limit)
    if hotels is None:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/hotels/{State}/{City}/", response_model=list[Hotel])
def hotels_by_State_and_City(State:str,City:str,skip: int = 0, limit: int = 50):
    hotels = showStrict(State=State,City=City,skip=skip,limit=limit)
    if hotels is None:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels


@app.get("/hotel/{City}/{Price}/", response_model=list[Hotel])
def hotels_by_City_and_Price(City:str,Price:int,skip: int = 0, limit: int = 50):
    hotels = CityPrice(City=City,Price=Price,skip=skip,limit=limit)
    if hotels is None:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels
    

@app.get("/hotel/{State}/{Price}/all/", response_model=list[Hotel])
def hotels_by_State_and_Price(State:str,Price:int,skip: int = 0, limit: int = 50):
    hotels = StatePrice(State=State,Price=Price,skip=skip,limit=limit)
    if hotels is None:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/cheap/", response_model=list[Hotel])
def Cheap_Hotels(skip: int = 0, limit: int = 50):
    hotels = Cheap(skip=skip,limit=limit)
    if hotels is None:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/moderate/", response_model=list[Hotel])
def Affordable_Hotels(skip: int = 0, limit: int = 50):
    hotels = Moderate(skip=skip,limit=limit)
    if hotels is None:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/expensive/", response_model=list[Hotel])
def Expensive_Hotels(skip: int = 0, limit: int = 50):
    hotels = Exotic(skip=skip,limit=limit)
    if hotels is None:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True)   
    
   