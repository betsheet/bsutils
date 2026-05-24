from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from bsutils.bookie.bookie import BookieEnum


class BetError(Enum):
    LOGIN_ERROR = "LoginError"
    SEARCHING_EVENT_ERROR = "SearchingEventError"
    EVENT_PAGE_ERROR = "EventPageError"
    NOT_IMPLEMENTED_MARKET_ERROR = "NotImplementedMarketError"
    NOT_IMPLEMENTED_MARKET_SPORT = "NotImplementedMarketSport"
    SELECTION_ERROR = "SelectionError"
    INVALID_SELECTION_FOR_MARKET = "InvalidSelectionForMarket"
    EVENT_NOT_FOUND = "EventNotFound"
    PLACER_MODAL_ERROR = "PlacerModalError"
    ODDS_BELOW_MINIMUM = "OddsBelowMinimum"
    UNAVAILABLE_SELECTION_ERROR = "UnavailableSelectionError"
    STAKING_ERROR = "StakingError"
    INSUFFICIENT_BANK = "InsufficientBankError"
    INACTIVE_ACCOUNT = "InactiveAccountError"
    OPENING_BLACK_SEARCH_EVENT_MODAL_ERROR = "OpeningBlackSearchEventModalError"
    MARKET_NOT_SUPPORTED_ERROR = "NotSupportedMarketError"
    UNEXPECTED_ERROR = "UnexpectedError"
    GENERIC_EXCEPTION = "GenericException"


class Bet(BaseModel):
    pick_id: str = Field(description="ID of the pick")
    user_id: str = Field(description="ID of the user")
    bookie: BookieEnum = Field(description="Bookie for the bet")
    stake: float = Field(description="Stake amount")
    placed_odds: Optional[float] = Field(default=None, description="Final odds the bet was placed with")
    is_placed: Optional[bool] = Field(default=False, description="Status indicating if bet is placed")
    placement_time: Optional[str] = Field(default=None, description="Placement timestamp string")
    placing_error: Optional[BetError] = Field(default=None, description="Error that occurred during placement")

    def raise_bet_exception(self, err: BetError):
        self.placing_error = err
        raise Exception(err.value)

    def set_placed_odds(self, odds: float):
        self.placed_odds = odds

    def set_as_placed(self, placed_value: bool, placed_odds: Optional[float] = None):
        self.is_placed = placed_value
        self.placement_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        if placed_odds is not None:
            self.set_placed_odds(placed_odds)

    def get_pick_id(self) -> str:
        return self.pick_id

    def __str__(self):
        # TODO: mejorar. que queden claros los campos relevantes
        return f"Bet[{self.bookie.value}] {self.pick_id}"
