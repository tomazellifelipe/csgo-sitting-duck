from typing import Dict, Optional
from pydantic import BaseModel, Field
from models.player_models import Player
from models.map_models import Map


class Previously(BaseModel):
    allplayers: Optional[Dict[str, Player]] = None
    map_info: Optional[Map] = Field(None, alias='map')


class Added(BaseModel):
    allplayers: Optional[Dict[str, Player]] = None
    map_info: Optional[Map] = Field(None, alias='map')
