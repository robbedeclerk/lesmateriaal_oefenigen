from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import Session, EV, ICE

#the get commands
def get_all(db):
    return db.query(EV).all() + db.query(ICE).all()

def get_id(set, id, db):
    return db.query(set).filter(set.id == id).all()

def get_year(set, year, db):
    return db.query(set).filter(set.year == year).all()

def get_model(set, model, db):
    return db.query(set).filter(set.model == model).all()

def get_price(set, price, db):
    return db.query(set).filter(set.price == price).all()

def get_range(set, range, db):
    return db.query(set).filter(set.range == range).all()

def get_brand(set, brand, db):
    return db.query(set).filter(set.brand == brand).all()

def get_id(set, id, db):
    return db.query(set).filter(set.id == id).all()

def get_fueltype(set, fueltype, db):
    return db.query(set).filter(set.fueltype == fueltype).all()

def get_mgp(set, mgp, db):
    return db.query(set).filter(set.mgp == mgp).all()

def get_pricelower(set, price, db):
    return db.query(set).filter(set.price <= price).all()

def get_pricehigher(set, price, db):
    return db.query(set).filter(set.price >= price).all()

#the delete commands

def delete_id_evs(set, id, db):
    db.query(set).filter(set.id == id).delete()
    #db.commit()
    return {"message": "id deleted"}

def delete_id_ices(set, id, db):
    db.query(set).filter(set.id == id).delete()
    #db.commit()
    return {"message": "id deleted"}
