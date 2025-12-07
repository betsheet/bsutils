# TODO: creo que debería estar en bsutils.apimodels.responses para leerlo cliente
from bsutils.base.base import BSBaseEntity


class LoginResponse(BSBaseEntity):
    user_id: str
    auth_token: str

class TelegramAppCredentialsResponse(BSBaseEntity):
    api_id: int
    api_hash: str