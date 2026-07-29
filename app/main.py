from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Root endpoint (Only for debugging purposes)
@app.get('/')
def root():
    return {"message": "OK"}

