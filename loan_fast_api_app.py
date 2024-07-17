from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

model_name = 'RF_Loan_model.joblib'
model = joblib.load(model_name)

#perform parsing
class LoanPred(BaseModel):
    Gender: float
    Married: float
    Dependents: float
    Education: float
    Self_Employed: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: float
    TotalIncome: float

@app.get