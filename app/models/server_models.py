from typing import Optional
from pydantic import BaseModel


class Bomb(BaseModel):
    state: Optional[str] = None
    position: Optional[str] = None
    countdown: Optional[str] = None
    player: Optional[str] = None


class PhaseCountdowns(BaseModel):
    phase: Optional[str] = None
    phase_ends_in: Optional[str] = None


class Provider(BaseModel):
    name: Optional[str] = None
    appid: Optional[int] = None
    version: Optional[int] = None
    steamid: Optional[str] = None
    timestamp: Optional[int] = None


class Round(BaseModel):
    phase: Optional[str] = None
    win_team: Optional[str] = None
    bomb: Optional[str] = None

