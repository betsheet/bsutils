from typing import Optional

from bsutils.base.base import BSBaseEntity
from bsutils.bookie.bsbookie import BSBookieEnum
from bsutils.pick.util import PickResult, PickSourceEnum, BSSelection, BSMarketEnum, PickSportEnum


# Pick class
class Pick(BSBaseEntity):
    user_id: Optional[str] = None  # el pick están siempre asociados al usuario que lo proporcionó.
    message_id: Optional[str] = None  # id del mensaje del que hemos obtenido el pick
    source: Optional[PickSourceEnum] = None

    bookie: Optional[BSBookieEnum] = None  # bookie para la que se publicó el pick, aunque la coloquemos en otra
    sport: Optional[PickSportEnum] = None
    competition_group: Optional[str] = None
    competition: Optional[str] = None

    date: Optional[str] = None
    time: Optional[str] = None
    is_live: bool = False

    participants: Optional[list[str]] = None  # se obtienen del string del event.

    selection: Optional[BSSelection] = None
    min_odds: Optional[float] = None
    stake_units: Optional[float] = None

    reception_time: Optional[str] = None
    result: Optional[PickResult] = None

    def get_event_string(self, separator: str = " vs. ") -> str:
        return f"{self.participants[0]}{separator}{self.participants[1]}"

    def set_id(self, id_: str) -> None:
        self.id_ = id_

    def __str__(self):
        return (f"{' v '.join(self.participants)} - {self.selection.market.value} "
                f"{self.selection.option.value if self.selection.option is not None else ''}{' - ' + self.selection.value if self.selection.value is not None else ''} @ {self.min_odds}")

    def to_str(self):
        return str(self)

class BetaminicPick(Pick):
    betaminic_strategy: Optional[str] = None  # en el futuro deberíamos tener un enum de estrategias
    email_message_id: Optional[str] = None

    def is_betaminic_1x2_pick(self) -> bool:
        return self.selection.market in [BSMarketEnum.RESULT]

    def is_betaminic_asian_pick(self) -> bool:
        return self.selection.market in [BSMarketEnum.TOTAL_GOALS, BSMarketEnum.ASIAN_HANDICAP]
