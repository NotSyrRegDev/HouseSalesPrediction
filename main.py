# main.py
from fastapi import FastAPI
from api.predict import router as predict_router

app = FastAPI()

app.include_router(predict_router)

# Start command:
# python service/train.py
# uvicorn main:app --reload