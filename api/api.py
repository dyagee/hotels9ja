from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
#from fastapi.encoders import jsonable_encoder
from api.routes import*
#from  models import Base
#from schemas import Hotel


app = FastAPI()


@app.get("/")
def docs_redirect():
    return RedirectResponse(url='/docs')
    
@app.get("/hotels/")
def all_hotels(skip: int = 0, limit: int = 100) -> list:
    hotels = showHotels( skip=skip, limit=limit)
    return hotels

@app.get("/hotel/{id}/")
def hotel_by_id(id:str):
    hotels = showByID(hotel_id=id)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotels

@app.get("/hotels/{State}")
def show_by_State(State:str,skip: int = 0, limit: int = 50)->list:
    hotels = showByState(State=State,skip=skip,limit=limit)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/hotels/{City}/")
def show_by_City(City:str,skip: int = 0, limit: int = 50) -> list:
    hotels = showByCity(City=City,skip=skip,limit=limit)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/hotels/{State}/{City}")
def hotels_by_State_and_City(State:str,City:str,skip: int = 0, limit: int = 50) -> list:
    hotels = showStrict(State=State,City=City,skip=skip,limit=limit)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels


@app.get("/hotel/{City}/{Price}/")
def hotels_by_City_and_Price(City:str,Price:int,skip: int = 0, limit: int = 50) -> list:
    hotels = CityPrice(City=City,Price=Price,skip=skip,limit=limit)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels
    

@app.get("/hotel/{State}/{Price}/all/")
def hotels_by_State_and_Price(State:str,Price:int,skip: int = 0, limit: int = 50) -> list:
    hotels = StatePrice(State=State,Price=Price,skip=skip,limit=limit)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/cheap/")
def Cheap_Hotels(skip: int = 0, limit: int = 50) -> list:
    hotels = Cheap(skip=skip,limit=limit)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/moderate/")
def Affordable_Hotels(skip: int = 0, limit: int = 50) -> list:
    hotels = Moderate(skip=skip,limit=limit)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels

@app.get("/expensive/")
def Expensive_Hotels(skip: int = 0, limit: int = 50) -> list:
    hotels = Exotic(skip=skip,limit=limit)
    if len(list(hotels)) == 0:
        raise HTTPException(status_code=404, detail="Hotels not Found")
    return hotels
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True)   
    
   