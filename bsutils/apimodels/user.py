from bsutils.base.base import BSBaseEntity


class BSUserCredentials(BSBaseEntity):
    email: str
    password: str

class UserStakeConfig(BSBaseEntity):
    pass

class UserTelegramData(BSBaseEntity):
    telegram_user_id: str
    phone_number: str    # with country code, e.g., +34123456789

class BSUser(BSBaseEntity):
    email: str | None
    credentials: BSUserCredentials
    stake_config: UserStakeConfig | None
    telegram_data: UserTelegramData | None
