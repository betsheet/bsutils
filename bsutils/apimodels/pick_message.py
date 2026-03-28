from bsutils.base.base import BSBaseEntity


class BSTelegramMessage(BSBaseEntity):
    telegram_message_id: str
    from_user_id: str  # id telegram del usuario que envía el mensaje (el que aporta el pick)
    from_telegram_chat_id: str  # id telegram del chat del que procede el mensaje
    content: str
    timestamp: str
