from pydantic import Field
from bsutils.base.base import BSBaseEntity


class AddTelegramListeningChannelRequest(BSBaseEntity):
    channel_username: str = Field(..., description="Telegram channel to listen from username", min_length=1)
    # TODO: podríamos definir así los campos para todos los modelos (con description y Field)ss