import pickle
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

model = pickle.load(open("../model/model.pkl", "rb"))

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
async def predict_species(data: IrisData):
    features = [[ data.sepal_length, data.sepal_width, data.petal_length, data.petal_width ]]
    predicted_class = model.predict(features)[0]
    return { "data": {"result": predicted_class}}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')