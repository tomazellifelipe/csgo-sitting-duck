from typing import Dict, Optional
from fastapi import Body, FastAPI
from models.player_models import AllPlayers
from models.map_models import Map
from pprint import pprint

app = FastAPI()

@app.post("/")
def root(map_info: Optional[Map] = Body(None, alias='map', embed=True), 
         allplayers: Optional[Dict[str, AllPlayers]] = Body(None, embed=True),
         previously: Optional[str] = Body(None, embed=True),
         added: Optional[str] = Body(None, embed=True)):
    return
