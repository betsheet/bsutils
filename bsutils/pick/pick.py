from typing import Optional

from pydantic import BaseModel, Field

from bsutils.bookie.bookie import BookieEnum
from bsutils.pick.util import PickResult, PickSourceEnum, BSSelection, PickMarketEnum, PickSportEnum


# Pick class
class Pick(BaseModel):
    id_: Optional[str] = Field(default=None, description="Pick identifier")
    user_id: Optional[str] = Field(default=None, description="User ID associated with the pick")
    message_id: Optional[str] = Field(default=None, description="Message ID from which the pick was obtained")
    source: Optional[PickSourceEnum] = Field(default=None, description="Source of the pick")

    bookie: Optional[BookieEnum] = Field(default=None, description="Bookie where the pick was published")
    sport: Optional[PickSportEnum] = Field(default=None, description="Sport of the event")
    competition_group: Optional[str] = Field(default=None, description="Group of the competition")
    competition: Optional[str] = Field(default=None, description="Competition name")

    date: Optional[str] = Field(default=None, description="Date of the event")
    time: Optional[str] = Field(default=None, description="Time of the event")
    is_live: bool = Field(default=False, description="Indicates if the event is live")

    participants: Optional[list[str]] = Field(default=None, description="List of participants in the event")

    selection: Optional[BSSelection] = Field(default=None, description="The selection/bet chosen")
    min_odds: Optional[float] = Field(default=None, description="Minimum odds for the pick")
    stake_units: Optional[float] = Field(default=None, description="Stake units for the pick")

    reception_time: Optional[str] = Field(default=None, description="Time when the pick was received")
    result: Optional[PickResult] = Field(default=None, description="Result of the pick")

    def get_event_string(self, separator: str = " vs. ") -> str:
        return f"{self.participants[0]}{separator}{self.participants[1]}"

    def set_id(self, id_: str) -> None:
        self.id_ = id_

    def _format_selection(self) -> str:
        if self.selection is None:
            return "N/A"
        if isinstance(self.selection, tuple):
            return f"{self.selection[0]} | {self.selection[1]}"
        return str(self.selection)

    def _format_market(self) -> str:
        if self.selection is None:
            return "N/A"
        if isinstance(self.selection, tuple):
            markets = {s.market.value for s in self.selection if s.market}
            return " | ".join(markets) if markets else "N/A"
        return self.selection.market.value if self.selection.market else "N/A"

    def __str__(self):
        participants_str = " v ".join(self.participants) if self.participants else "N/A"
        lines = [
            "📋 Pick",
            f"  🏟️  Event:        {participants_str}",
            f"  ⚽  Sport:        {self.sport.value if self.sport else 'N/A'}",
            f"  🏆  Competition:  {self.competition or 'N/A'}",
            f"  📅  Date:         {self.date or 'N/A'} {self.time or ''}".rstrip(),
            f"  🎯  Market:       {self._format_market()}",
            f"  ✅  Selection:    {self._format_selection()}",
            f"  💰  Min. odds:    {self.min_odds if self.min_odds is not None else 'N/A'}",
            f"  📊  Stake:        {self.stake_units if self.stake_units is not None else 'N/A'}",
            f"  🏦  Bookie:       {self.bookie.value if self.bookie else 'N/A'}",
            f"  📡  Source:       {self.source.value if self.source else 'N/A'}",
            f"  🔴  Live:         {'Yes' if self.is_live else 'No'}",
            f"  🕐  Reception:    {self.reception_time or 'N/A'}",
            f"  🏁  Result:       {self.result.value if self.result else 'N/A'}",
        ]
        return "\n".join(lines)

    def to_str(self):
        return str(self)

