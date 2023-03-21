from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fractions import Fraction
import pickle
import pandas as pd
from fastapi.encoders import jsonable_encoder

class InputData(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

with open('svm_project.pkl', 'rb') as f:
    model1 = pickle.load(f)

app = FastAPI()

@app.post('/prediction')
def get_prediction(data: InputData):
    received = pd.DataFrame(jsonable_encoder(data), index=[0])
    cols_new = ['V1', 'V2', 'V3', 'V4','V5', 'V6', 'V7','V8', 'V9', 'V10', 'V11','V12', 'V13', 'V14', 'V15','V16', 'V17', 'V18','V19', 'V20','V21', 'V22','V23', 'V24','V25', 'V26','V27', 'V28','Amount']

    received = received[cols_new]
    pred_name = model1.predict(received)[0]
    Prob = model1.predict_proba(received) * 100
    probability_percent = {
			"Froud_odds": round(Prob.tolist()[0][0], 2),
			"Nofroud_odds": round(Prob.tolist()[0][1], 2)
	}
    decimal_odds = {
		"Froud_odds": round(100/Prob.tolist()[0][0], 2),
		"Nofroud_odds": round(100/Prob.tolist()[0][1], 2)
    }

    return {'prediction': pred_name,
			'probability_percent': probability_percent,
			"predicted_decimal_odds": decimal_odds
			
			}
