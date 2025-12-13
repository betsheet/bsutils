from bsutils.base.base import BSBaseEntity


class BSUserCredentials(BSBaseEntity):
    email: str
    password: str

class UserStakeConfig(BSBaseEntity):
    user_id: str

class UserTelegramData(BSBaseEntity):
    user_id: str
    phone_number: str    # with country code, e.g., +34123456789
    telegram_id: str

class BSUser(BSBaseEntity):
    email: str | None
    credentials: BSUserCredentials
    stake_config: UserStakeConfig | None
    telegram_data: UserTelegramData | None
