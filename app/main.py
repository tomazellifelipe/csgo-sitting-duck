from typing import Dict, Optional
from fastapi import Body, FastAPI
from models.player_models import Player
from models.map_models import Map
from models.misc_models import Previously, Added


app = FastAPI()

@app.post("/")
def root(map_info: Optional[Map] = Body(None, alias='map', embed=True), 
         allplayers: Optional[Dict[str, Player]] = Body(None, embed=True),
         previously: Optional[Previously] = Body(None, embed=True),
         added: Optional[Added] = Body(None, embed=True)):
    return
