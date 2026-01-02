from bsutils.base.base import BSBaseEntity


class BSPickMessage(BSBaseEntity):
    from_user_id: str  # id telegram del usuario que envía el mensaje (el que aporta el pick)
    content: str
    timestamp: str

class BSTelegramPickMessage(BSPickMessage):
    from_telegram_chat_id: str  # id telegram del chat del que procede el mensaje