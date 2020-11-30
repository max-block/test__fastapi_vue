from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return str(v)


class MongoModel(BaseModel):
    def to_doc(self) -> dict:
        doc = self.dict()
        if doc["id"] is not None:
            doc["_id"] = doc["id"]
        del doc["id"]
        return doc


class Data1(MongoModel):
    id: Optional[ObjectIdStr] = Field(None, alias="_id")
    name: str
    value: int
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Data2(MongoModel):
    id: Optional[ObjectIdStr] = Field(None, alias="_id")
    name: str
    tags: list[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
