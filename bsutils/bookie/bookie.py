from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class BookieEnum(Enum):
    BLACK_BETINASIA = "BlackBetInAsia"
    SPORTIUM = "Sportium"
    BET_365 = "Bet365"
    PS3838 = "PS3838"
    _1XBET = "1xbet"
    LADBROKES = "Ladbrokes"
    BETFAIR = "Betfair"
    SPORTAZA = "Sportaza"
    BWIN = "Bwin"
    KAMBI = "Kambi"
    PINNACLE = "Pinnacle"
    CASINIA = "Casinia"
    NONE = "None"


class Bookie(BaseModel):
    """ Represents models from 'bookie' collection"""
    bookie_id: Optional[str] = Field(..., description="Unique identifier of the bookie", min_length=1)
    name: BookieEnum = Field(..., description="Name of the bookie")


class BookieCredentials(BaseModel):
    """ Represents models from 'bookie_credentials' collection"""
    user_id: Optional[str]
    bookie: BookieEnum
    username: str
    password: str
    url: str
