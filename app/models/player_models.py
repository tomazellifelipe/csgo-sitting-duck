from typing import Dict, Optional, Union

from gamestate.read_cfg import payload_config
from pydantic import BaseModel, Field


class MatchStats(BaseModel):
    kills: Optional[int] = None
    assists: Optional[int] = None
    deaths: Optional[int] = None
    mvps: Optional[int] = None
    score: Optional[int] = None


class PlayerID(BaseModel):
    steamid: Optional[str] = None
    clan: Optional[str] = None
    name: Optional[str] = None
    observer_slot: Optional[int] = None
    team: Optional[str] = None
    activity: Optional[str] = None


class Position(BaseModel):
    spectarget: Optional[str] = None
    forward: Optional[str] = None
    position: Optional[str] = None
    

class State(BaseModel):
    health: Optional[int] = None
    armor: Optional[int] = None
    helmet: Optional[bool] = None
    flashed: Optional[int] = None
    smoked: Optional[int] = None
    burning: Optional[int] = None
    money: Optional[int] = None
    round_kills: Optional[int] = None
    round_killshs: Optional[int] = None
    equip_value: Optional[int] = None


class Weapons(BaseModel):
    name: Optional[str] = None
    paintkit: Optional[str] = None
    weapon_type: Optional[str] = Field(None, alias='type')
    ammo_clip: Optional[int] = None
    ammo_clip_max: Optional[int] = None
    ammo_reserve: Optional[int] = None
    state: Optional[str] = None


class Player(Position, PlayerID):
    state: Optional[State] = None
    match_stats: Optional[MatchStats] = None
    weapons: Optional[Dict[str, Union[Weapons, bool]]] = None
    
