from typing import Any, Annotated
from bson import ObjectId
from pydantic import BaseModel, Field


class BSBaseEntity(BaseModel):
    id_: Annotated[str | None, Field(alias="_id")] = None

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    def as_json(self):
        return self.model_dump(by_alias=True, mode='json')

    def get_object_id(self) -> ObjectId:
        return ObjectId(self.id_)
