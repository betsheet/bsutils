from enum import Enum
from bsutils.base.base import BSBaseEntity
from bsutils.bookie.bsbookie import BSBookieEnum
from bsutils.pick.util import PickSourceEnum, BSSelection, BSMarketEnum, PickSportEnum


class PickResult(Enum):
    SUCCESS = "Success"
    FAIL = "Fail"
    NULL = "Null"

# Pick class
class Pick(BSBaseEntity):
    # TODO cambiar a formato Optional[]
    user_id: str | None = None  # el pick están siempre asociados al usuario que lo proporcionó.
    message_id: str | None = None  # id del mensaje del que hemos obtenido el pick
    source: PickSourceEnum | None = None

    bookie: BSBookieEnum | None = None  # bookie para la que se publicó el pick, aunque la coloquemos en otra
    sport: PickSportEnum | None = None
    competition_group: str | None = None
    competition: str | None = None

    date: str | None = None
    time: str | None = None
    is_live: bool = False

    participants: list[str] | None = None  # se obtienen del string del event.

    selection: BSSelection | None = None
    min_odds: float | None = None
    stake_units: float | None = None

    reception_time: str | None = None
    result: PickResult | None = None

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
    betaminic_strategy: str | None = None  # en el futuro deberíamos tener un enum de estrategias
    email_message_id: str | None = None

    def is_betaminic_1x2_pick(self) -> bool:
        return self.selection.market in [BSMarketEnum.RESULT]

    def is_betaminic_asian_pick(self) -> bool:
        return self.selection.market in [BSMarketEnum.TOTAL_GOALS, BSMarketEnum.ASIAN_HANDICAP]
