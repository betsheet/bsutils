from bsutils.apimodels.user import UserTelegramData, UserStakeConfig
from bsutils.base.base import BSBaseEntity


class LoginResponse(BSBaseEntity):
    user_id: str
    auth_token: str


class TelegramAppCredentialsResponse(BSBaseEntity):
    api_id: int
    api_hash: str


class BSUserDataResponse(BSBaseEntity):
    user_id: str
    email: str
    telegram_data: UserTelegramData
    stake_config: UserStakeConfig
