from typing import Dict, Optional

from pydantic import BaseModel, Field

from models.map_models import Map
from models.player_models import Player
from models.server_models import Bomb, PhaseCountdowns, Round


class Added(BaseModel):
    player: Optional[Player] = None
    allplayers: Optional[Dict[str, Player]] = None
    bomb: Optional[Bomb] = None
    map_info: Optional[Map] = Field(None, alias='map')
    phase_countdowns: Optional[PhaseCountdowns] = None 
    round_phase: Optional[Round] = Field(None, alias='round')


class Previously(BaseModel):
    player: Optional[Player] = None
    allplayers: Optional[Dict[str, Player]] = None
    bomb: Optional[Bomb] = None
    map_info: Optional[Map] = Field(None, alias='map')
    phase_countdowns: Optional[PhaseCountdowns] = None 
    round_phase: Optional[Round] = Field(None, alias='round')


