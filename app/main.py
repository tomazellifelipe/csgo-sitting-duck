from typing import Dict, Optional

from fastapi import Body, FastAPI

import gamestate.read_cfg
from models.map_models import Map
from models.misc_models import Added, Previously 
from models.player_models import Player
from models.server_models import Bomb, PhaseCountdowns, Provider, Round


app = FastAPI()

@app.post("/observer")
def observer(allplayers: Optional[Dict[str, Player]] = Body(None, embed=True),
             bomb: Optional[Bomb] = Body(None, embed=True),
             map_info: Optional[Map] = Body(None, alias='map', embed=True), 
             phase_countdowns: Optional[PhaseCountdowns] = Body(None, embed=True),
             provider: Optional[Provider] = Body(None, embed=True),
             round_phase: Optional[Round] = Body(None, alias='round', embed=True),
             previously: Optional[Previously] = Body(None, embed=True),
             added: Optional[Added] = Body(None, embed=True)):
    return

@app.post("/live")
def live(map_info: Optional[Map] = Body(None, alias='map', embed=True), 
         player: Optional[Player] = Body(None, embed=True),
         provider: Optional[Provider] = Body(None, embed=True),
         round_phase: Optional[Round] = Body(None, alias='round', embed=True),
         previously: Optional[Previously] = Body(None, embed=True),
         added: Optional[Added] = Body(None, embed=True)):
    return
