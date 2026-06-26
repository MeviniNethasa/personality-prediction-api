from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pandas as pd
import joblib


app=FastAPI(title="Personality Prediciton API")
model=joblib.load("model.pkl")

class PersonData(BaseModel):
  Time_spent_Alone: float
  Stage_fear: int                  
  Social_event_attendance: float
  Going_outside: float
  Drained_after_socializing: int   
  Friends_circle_size: float
  Post_frequency: float

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r") as file:
        return file.read()

@app.post("/predict")
def predict(data: PersonData):
    input_df = pd.DataFrame([data.model_dump()])  
    prediction = int(model.predict(input_df)[0])
    personality = "Extrovert" if prediction == 1 else "Introvert"
    return {"personality": personality}