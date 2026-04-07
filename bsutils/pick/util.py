from enum import Enum
from typing import Optional, Union
from typing_extensions import override
from bsutils.base.base import BSBaseEntity


class PickResult(Enum):
    SUCCESS = "Success"
    FAIL = "Fail"
    NULL = "Null"


class PickSourceEnum(Enum):
    BETAMINIC = "Betaminic"
    ODDS_NOTIFIER = "OddsNotifier"
    TOM_WHITAKER = "TomWhitaker"
    BLOGABET = "Blogabet"
    WINNER_ODDS = "WinnerOdds"
    BETAMINIC_BETTING_SHOTS = "BetaminicBettingShots"
    INPLAY_FOOTBALL_TIPS = "InplayFootballTips"
    BETTING_SIGNALS = "BettingSignals"
    SOLOPICKS = "Solopicks"
    TEST = "Test"


class PickSportEnum(Enum):
    FOOTBALL = "Soccer"  # le ponemos soccer en vez de football porque así aparece la clase en Sportium
    BASKETBALL = "Basketball"
    VOLLEYBALL = "Volleyball"
    TENNIS = "Tennis"
    HANDBALL = "Handball"
    HORSE_RACING = "HorseRacing"
    ICE_HOCKEY = "IceHockey"
    ESPORTS = "E-Sports"
    FLOORBALL = "Floorball"


class BSMarketEnum(Enum):
    RESULT = "1x2"
    HANDICAP = "Handicap"
    HALF_TIME_HANDICAP = "HalfTimeHandicap"
    ASIAN_HANDICAP = "AsianHandicap"
    HALF_TIME_ASIAN_HANDICAP = "HalfTimeAsianHandicap"  # 1st Half Asian Handicap
    TOTAL_GOALS = "TotalGoals"
    GAME_LINES = "GameLines"
    HALF_TIME_TOTAL_GOALS = "HalfTimeTotalGoals"
    TOTALS = "Totals"   # TODO: cambiar a TOTAL
    PARTICIPANT_TOTAL = "ParticipantTotal"
    PARTICIPANT_HALF_TIME_TOTAL = "ParticipantHalfTimeTotal"
    SPREAD = "Spread"
    MONEY_LINE = "MoneyLine"
    TO_WIN = "ToWin"
    HORSE_RACING = "HorseRacing"
    NONE = "None"


class BSSelectionOptionEnum(Enum):
    HOME = "Home"
    DRAW = "Draw"
    AWAY = "Away"
    OVER = "Over"
    UNDER = "Under"
    HORSE = "Horse"
    NONE = "None"


class BSSelection(BSBaseEntity):
    market: BSMarketEnum
    option: Union[BSSelectionOptionEnum, tuple[BSSelectionOptionEnum, BSSelectionOptionEnum]]
    value: Optional[str]

    @staticmethod
    def empty_selection() -> "BSSelection":
        return BSSelection(market=BSMarketEnum.NONE, option=BSSelectionOptionEnum.NONE, value=None)

    @override
    def as_json(self):
        json_dict: dict = self.model_dump(by_alias=True, mode='json')
        del json_dict['_id']
        return json_dict

    def __str__(self):
        return f"{self.market.value if self.market is not None else ''} - {self.option} {self.value if self.value is not None else ''}".strip()