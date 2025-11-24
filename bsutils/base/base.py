from typing import Any
from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict


class BSBaseEntity(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    id_: str | None = Field(default=None, alias="_id")

    def __init__(self, /, **data: Any):
        super().__init__(**data)

    def as_json(self):
        return self.model_dump(by_alias=True, mode='json')

    def get_object_id(self) -> ObjectId:
        return ObjectId(self.id_)
