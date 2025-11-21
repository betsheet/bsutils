from bsutils.base.base import BSBaseEntity


class BSUserCredentials(BSBaseEntity):
    username: str
    password: str


class BSUser(BSBaseEntity):
    email: str | None
    credentials: BSUserCredentials
