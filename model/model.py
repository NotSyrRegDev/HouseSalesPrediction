#Loading the generate model house_price_model.pkl

# model/model.py
import joblib
import os

class HousePriceModel:
    def __init__(self):
        model_path = os.path.join("model", "house_price_model.pkl")
        self.model = joblib.load(model_path)
    
    def predict_price(self, sqft_living, bedrooms, bathrooms, yr_built):
        features = [[sqft_living, bedrooms, bathrooms, yr_built]]
        return self.model.predict(features)[0]
    