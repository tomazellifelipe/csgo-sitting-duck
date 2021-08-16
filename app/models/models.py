from typing import Optional

from pydantic import BaseModel


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


class Position(BaseModel):
    forward: Optional[str] = None
    position: Optional[str] = None


class PlayerID(BaseModel):
    clan: Optional[str] = None
    name: Optional[str] = None
    observer_slot: Optional[int] = None
    team: Optional[str] = None
    activity: Optional[str] = None


class Player(Position, PlayerID):
    state: Optional[State] = None


class AllPlayers(Player):
    pass
