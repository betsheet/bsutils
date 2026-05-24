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
    id_: Optional[str] = Field(..., description="Unique identifier of the bookie", min_length=1)
    name: BookieEnum = Field(..., description="Name of the bookie")


class BookieCredentials(BaseModel):
    """ Represents models from 'bookie_credentials' collection"""
    id_: Optional[str] = Field(default=None, alias="_id", description="ID in the MongoDB collection")
    user_id: Optional[str] = Field(default=None, description="ID of the user")
    bookie: BookieEnum = Field(description="Bookie enum associated with the credentials")
    username: str = Field(description="Username for the bookie login")
    password: str = Field(description="Password for the bookie login")
    url: str = Field(description="Login URL of the bookie")
