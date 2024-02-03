from fastapi import FastAPI
import json

with open("data.json") as file:
    data=json.load(file)

app=FastAPI()
evs=data["EVs"]

@app.get("/")
def read_root():
    return data

@app.get("/EVs/{car_id}")
def read_car(car_id: int):
    return data["EVs"][car_id]

@app.get("/EVs/models/{model}")
def read_car(model:str):
    return [car for car in data ["EVs"] if car["model"].lower() == model.lower()]

@app.get("/EVs/year/{year}")
def read_car(year:int):
    return get_year(evs,year)

def get_year(set,year):
    return [car for car in set if car["year"] == year]

@app.get("/pricelower/{price}")
def read_price(price:int):
    return get_pricelower(evs,price)


def get_pricelower(set,price):
    return [car for car in set if car["price"] <= price]

@app.delete('/EVs/{car_id}')
def delete_car(car_id:int):
    evs.pop(car_id)
    #with open('data.json','w') as file:
    #    json.dump(data,file)
    return {"message":"car deleted"}

@app.put('/EVs/{car_id}/year/{new_year}')
def update_year(car_id:int,new_year:int):
    evs[car_id]["year"] = new_year
    #with open('data.json','w') as file:
    #    json.dump(data,file)
    return {"message":"year updated"}