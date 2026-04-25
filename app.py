import uvicorn
from fastapi import FastAPI
from validation import validation
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
f = open('model.pkl','rb')
model = pickle.load(f)

@app.post('/predict')
def model_prediction(data: validation):
    
    prediction = model.predict([[
        data.variance,
        data.skewness,
        data.curtosis,
        data.entropy
    ]])

    if prediction[0] > 0.5:
        result = "Fake note"
    else:
        result = "Its a Bank note"

    return {
        'prediction': result
    }
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)