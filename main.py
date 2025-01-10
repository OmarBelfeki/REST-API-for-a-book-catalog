from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status, Query

@app.get(path="/", response_model=dict)
def welcome():
    return {"welcome": "REST API for a book catalog"}
