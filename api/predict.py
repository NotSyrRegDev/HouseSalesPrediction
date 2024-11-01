# api/predict.py
# File resposible for predict route 

from fastapi import APIRouter
from pydantic import BaseModel
from model.model import HousePriceModel

router = APIRouter()
model = HousePriceModel()

# request body
class HouseData(BaseModel):
    sqft_living: float
    bedrooms: int
    bathrooms: float
    yr_built: int

#Defening predict route

@router.post("/predict")
def predict_price(data: HouseData):
    #method from model
    price = model.predict_price(
        sqft_living=data.sqft_living,
        bedrooms=data.bedrooms,
        bathrooms=data.bathrooms,
        yr_built=data.yr_built
    )
    return {"predicted_price": price}