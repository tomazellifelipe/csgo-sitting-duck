from typing import Dict, Optional

from pydantic import BaseModel

from gamestate.read_cfg import payload_config
from models.map_models import Map
from models.misc_models import Added, Previously 
from models.player_models import Player
from models.server_models import Bomb, PhaseCountdowns, Provider, Round


class Payload(BaseModel):
    if any(key in "player_" for key in payload_config.keys()):
        player: Optional[Players] = None
    if any(key in "allplayers" for key in payload_config.keys()):
        allplayers: Optional[Dict[str, Player]] = None
    if "bomb" in payload_config.keys():
        bomb: Optional[Bomb] = None
    if any(key in "map" for key in payload_config.keys()):
        map_info: Optional[Map] = None
    if "phase_countdowns" in payload_config.keys():
        phase_countdowns: Optional[PhaseCountdowns] = None 
    if "provider" in payload_config.keys():
        provider: Optional[Provider] = None
    if "round" in payload_config.keys():
        round_phase: Optional[Round] = None
    previously: Optional[Previously] = None
    added: Optional[Added] = None

