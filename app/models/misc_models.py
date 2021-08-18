from typing import Dict, Optional

from pydantic import BaseModel, Field

from models.map_models import Map
from models.player_models import Player
from models.server_models import Bomb, PhaseCountdowns, Round


class Added(BaseModel):
    allplayers: Optional[Dict[str, Player]] = None
    bomb: Optional[Bomb] = None
    map_info: Optional[Map] = Field(None, alias='map')
    player: Optional[Player] = None
    phase_countdowns: Optional[PhaseCountdowns] = None
    round_phase: Optional[Round] = Field(None, alias='round')


class Previously(BaseModel):
    allplayers: Optional[Dict[str, Player]] = None
    bomb: Optional[Bomb] = None
    map_info: Optional[Map] = Field(None, alias='map')
    player: Optional[Player] = None
    phase_countdowns: Optional[PhaseCountdowns] = None
    round_phase: Optional[Round] = Field(None, alias='round')

