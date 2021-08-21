from typing import Dict, Optional

from pydantic import BaseModel, Field

from models.map_models import Map
from models.misc_models import Added, Previously 
from models.player_models import Player
from models.server_models import Bomb, PhaseCountdowns, Provider, Round


class Payload(BaseModel):
    player: Optional[Player] = None
    allplayers: Optional[Dict[str, Player]] = None 
    bomb: Optional[Bomb] = None
    map_info: Optional[Map] = Field(None, alias='map')
    phase_countdowns: Optional[PhaseCountdowns] = None 
    provider: Optional[Provider] = None
    round_phase: Optional[Round] = Field(None, alias='round')
    previously: Optional[Previously] = None
    added: Optional[Added] = None

