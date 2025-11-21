from enum import Enum
from bsutils.base.base import BSBaseEntity


class BSBookieEnum(Enum):
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
    NONE = "None"

# TODO: Esta clase quizás debería estar en el paquete del cliente.
# esto no debemos guardarlo nunca en nuestra base de datos, sino en el cliente
class BSBookieCredentials(BSBaseEntity):
    bookie: BSBookieEnum
    username: str
    password: str
    url: str
