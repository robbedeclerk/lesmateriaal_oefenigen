# from fastapi import FastAPI
# import json

# with open("data.json") as file:
#     data = json.load(file)

# evs = data["EVs"]
# ices = data["ICEs"]

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return data

# @app.get("/evs/{car_id}")
# def read_car(car_id: int):
#     return evs[car_id]

# @app.get("/ices/{car_id}")
# def read_car(car_id: int):
#     return ices[car_id]

# @app.get("/evs/model/{model}")
# def read_model(model: str):
#     return [car for car in evs if car["model"].lower() == model.lower()]

# @app.get("evs/year/{year}")
# def read_year(year: int):
#     return get_year(evs, year)

# @app.get("/year/{year}")
# def read_year(year: int):
#     return get_year(evs, year) + get_year(ices, year)

# @app.get("/price/{operation}/{price}")
# def read_price(price: int, operation: str):
#     if operation == "lower":
#         return get_pricelower(evs, price) + get_pricelower(ices, price)
#     if operation == "higher":
#         return get_pricehigher(evs, price) + get_pricehigher(ices, price)

# @app.put("/evs/{car_id}/year/{new_year}")
# def update_year(car_id: int, new_year: int):
#     evs[car_id]["year"] = new_year
    
#     # with open("data.json", "w") as file:
#     #     json.dump(data, file)
    
#     return {
#         "message": "Year updated successfully",
#         "car": evs[car_id]
#     }

# @app.put("/evs/{car_id}/price/{new_price}")
# def update_year(car_id: int, new_price: int):
#     evs[car_id]["price"] = new_price
    
#     # with open("data.json", "w") as file:
#     #     json.dump(data, file)
    
#     return {
#         "message": "Price updated successfully",
#         "car": evs[car_id]
#     }

# @app.delete("/evs/{car_id}")
# def delete_car(car_id: int):
#     evs.pop(car_id)
    
#     # with open("data.json", "w") as file:
#     #     json.dump(data, file)
    
#     return {"message": "EV deleted successfully"}

# def get_year(set, year):
#     return [car for car in set if car["year"] == year]

# def get_pricelower(set, price):
#     return [car for car in set if car["price"] <= price]

# def get_pricehigher(set, price):
#     return [car for car in set if car["price"] >= price]