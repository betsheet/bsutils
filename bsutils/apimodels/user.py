from bsutils.base.base import BSBaseEntity


class BSUserCredentials(BSBaseEntity):
    email: str
    password: str

class UserStakeConfig(BSBaseEntity):
    # TODO: completar
    user_id: str

class UserTelegramData(BSBaseEntity):
    user_id: str
    phone_number: str    # with country code, e.g., +34123456789
    telegram_id: str
    listening_channels: list[str] = []

class BSUser(BSBaseEntity):
    email: str | None
    credentials: BSUserCredentials