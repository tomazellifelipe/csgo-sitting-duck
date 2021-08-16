from typing import Dict, Optional
from fastapi import Body, FastAPI
from models.player_models import AllPlayers 
from pprint import pprint

app = FastAPI()

@app.post("/")
def root(payload: AllPlayers):
    pprint(payload)
    return payload
