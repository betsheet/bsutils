from bsutils.base.base import BSBaseEntity


class BSPickMessage(BSBaseEntity):
    from_user_id: str  # id telegram del usuario que envía el mensaje
    content: str

# TODO: igual lo quitamos
class BSTelegramPickMessage(BSBaseEntity):
    from_user_id: str  # id telegram del usuario que envía el mensaje
    content: str