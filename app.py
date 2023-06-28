from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

model = pickle.load(open("models/model.pkl", "rb"))

@app.post("/predict")
async def predict_species(data: IrisData):
    features = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    predicted_class = model.predict(features)[0]
    return {"species": predicted_class}
