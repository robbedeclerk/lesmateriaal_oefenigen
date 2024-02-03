from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import Session, EV, ICE
from comands import *

app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return get_all(db)

@app.get("/ev/{id}")
def read_ev(id: int, db: Session = Depends(get_db)):
    return db.query(EV).filter(EV.id == id).first() 

@app.get("/id/{id}")
def read_id(id:str, db: Session = Depends(get_db)):
    return get_id(EV, id, db) + get_id(ICE, id, db)

@app.get("/year/{year}")
def read_year(year: int, db: Session = Depends(get_db)):
    return get_year(EV, year, db) + get_year(ICE, year, db)

@app.get("/model/{model}")
def read_model(model:str, db: Session = Depends(get_db)):
    return get_model(EV, model, db) + get_model(ICE, model, db)

@app.get("/price/{price}")
def read_price(price:int, db: Session = Depends(get_db)):
    return get_price(EV, price, db) + get_price(ICE, price, db)

@app.get("/range/{range}")
def read_range(range:int, db: Session = Depends(get_db)):
    return get_range(EV, range, db)

@app.get("/brand/{brand}")
def read_brand(brand:str, db: Session = Depends(get_db)):
    return get_brand(EV, brand, db) + get_brand(ICE, brand, db)

@app.get("/fueltype/{fueltype}")
def read_fueltype(fueltype:str, db: Session = Depends(get_db)):
    return get_fueltype(ICE, fueltype, db)

@app.get("/mgp/{mgp}")
def read_mgp(mgp:int, db: Session = Depends(get_db)):
    return get_mgp(ICE, mgp, db)

@app.get("/price/{operation}/{price}")
def read_price(price: int, operation: str, db: Session = Depends(get_db)):
    if operation == "lower":
        return get_pricelower(EV, price, db) + get_pricelower(ICE, price, db)
    if operation == "higher":
        return get_pricehigher(EV, price, db) + get_pricehigher(ICE, price, db)


@app.delete("/ev/{id}")
def delete_ev(id: int, db: Session = Depends(get_db)):
    db.query(EV).filter(EV.id == id).delete()
    #db.commit()
    return {"message": "EV deleted"}

