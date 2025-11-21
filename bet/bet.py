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

    def set_as_placed(self, placed_value: bool):
        self.is_placed = placed_value
        self.placement_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def get_pick_id(self) -> ObjectId:
        return ObjectId(self.pick_id)

    def __str__(self):
        status = "✓ Placed" if self.is_placed else "✗ Failed"
        error_str = f" ({self.placing_error.value})" if self.placing_error else ""
        odds_str = f" @ {self.placed_odds}" if self.placed_odds else ""
        time_str = f" at {self.placement_time}" if self.placement_time else ""
        
        return f"Bet[{self.bookie.value}] {self.id_}"