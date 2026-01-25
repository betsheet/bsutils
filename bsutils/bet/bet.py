from datetime import datetime
from enum import Enum
from typing import Optional
from bson import ObjectId
from bsutils.base.base import BSBaseEntity
from bsutils.bookie.bsbookie import BSBookieEnum


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
    UNEXPECTED_ERROR = "UnexpectedError"
    GENERIC_EXCEPTION = "GenericException"


class Bet(BSBaseEntity):
    pick_id: str
    user_id: str
    bookie: BSBookieEnum
    stake: float
    placed_odds: Optional[float] | None = None
    is_placed: Optional[bool] | None = False
    placement_time: str | None = None
    placing_error: Optional[BetError] | None = None

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

    def get_pick_id(self) -> ObjectId:
        return ObjectId(self.pick_id)

    def __str__(self):
        return f"Bet[{self.bookie.value}] {self.id_}"