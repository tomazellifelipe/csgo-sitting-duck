from typing import Dict, Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from models.models import AllPlayers 

app = FastAPI()

@app.post("/")
def root(allplayers: Dict[str, AllPlayers]):
    return allplayers
