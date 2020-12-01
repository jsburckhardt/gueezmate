from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
from helper import total_expenses


app = FastAPI()

class Expense(BaseModel):
    date: datetime
    weekly_expense: bool
    expense: float
    store: str
    expense_type: str



database = []

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.get("/v1/health")
def read_health():
    return {"Status": "Healthy"}

@app.post("/v1/ingest")
def ingest_income(expense: Expense):
    database.append(expense.dict())
    return total_expenses(database)

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}