from typing import Any, Optional
from bson import ObjectId
from pydantic import BaseModel, Field


class BSBaseEntity(BaseModel):
    id_: Optional[str | None] = Field(None, alias="_id")

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    def as_json(self):
        return self.model_dump(by_alias=True, mode='json')

    def get_object_id(self) -> ObjectId:
        return ObjectId(self.id_)
