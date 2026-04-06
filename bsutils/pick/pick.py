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
        participants_str = " v ".join(self.participants) if self.participants else "N/A"
        lines = [
            "📋 Pick",
            f"  🏟️  Evento:       {participants_str}",
            f"  ⚽  Deporte:      {self.sport.value if self.sport else 'N/A'}",
            f"  🏆  Competición:  {self.competition or 'N/A'}",
            f"  📅  Fecha:        {self.date or 'N/A'} {self.time or ''}".rstrip(),
            f"  🎯  Mercado:      {self.selection.market.value if self.selection else 'N/A'}",
            f"  ✅  Selección:    {str(self.selection) if self.selection else 'N/A'}",
            f"  💰  Cuota mín.:  {self.min_odds if self.min_odds is not None else 'N/A'}",
            f"  📊  Stake:        {self.stake_units if self.stake_units is not None else 'N/A'}",
            f"  🏦  Bookie:       {self.bookie.value if self.bookie else 'N/A'}",
            f"  📡  Fuente:       {self.source.value if self.source else 'N/A'}",
            f"  🔴  En vivo:      {'Sí' if self.is_live else 'No'}",
            f"  🏁  Resultado:    {self.result.value if self.result else 'N/A'}",
        ]
        return "\n".join(lines)

    def to_str(self):
        return str(self)

class BetaminicPick(Pick):
    betaminic_strategy: Optional[str] = None  # en el futuro deberíamos tener un enum de estrategias
    email_message_id: Optional[str] = None

    def is_betaminic_1x2_pick(self) -> bool:
        return self.selection.market in [BSMarketEnum.RESULT]

    def is_betaminic_asian_pick(self) -> bool:
        return self.selection.market in [BSMarketEnum.TOTAL_GOALS, BSMarketEnum.ASIAN_HANDICAP]
