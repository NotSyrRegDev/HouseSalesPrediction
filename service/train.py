# service/train.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

def train_model():
    # Load the dataset
    df = pd.read_csv("kc_house_data.csv")
    
    # Selected columns
    features = df[["sqft_living", "bedrooms", "bathrooms", "yr_built"]]
    target = df["price"]
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the model
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/house_price_model.pkl")
    print("Model training completed and saved to model/house_price_model.pkl")

if __name__ == "__main__":
    train_model()