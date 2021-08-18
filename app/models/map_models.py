from typing import Dict, Optional

from pydantic import BaseModel, Field


class Team(BaseModel):
    score: Optional[int] = None
    consecutive_round_losses: Optional[int] = None
    timeouts_remaining: Optional[int] = None
    matches_won_this_series: Optional[int] = None


class MapInfo(BaseModel):
    mode: Optional[str] = None
    name: Optional[str] = None
    phase: Optional[str] = None
    match_round: Optional[int] = Field(None, alias='round')
    team_ct: Optional[Team] = None
    team_t: Optional[Team] = None
    num_matches_to_win_series: Optional[int] = None 
    current_spectators: Optional[int] = None 
    souvenier_total: Optional[int] = None


class RoundInfo(BaseModel):
    round_wins: Optional[Dict[str, str]] = None


class Map(MapInfo, RoundInfo):
    pass

