from pydantic import BaseModel
from enum import Enum


class CreateKongConsumer(BaseModel):
    username: str
    custom_id: str

    class Config:
        schema_extra = {
            "example": {
                "username": "my_username",
                "custom_id": "my_custom_id"
            }
        }

class KongConsumer(BaseModel):
    id: str
    custom_id: str
    tags: str = None
    created_at: int
    username: str


class KongConsumerAttributes(str, Enum):
    kong_consumer_id = 'kong_consumer_id'
    id = 'id'
    username = 'username'
    custom_id = 'custom_id'
    tags = 'tags'
    created_at = 'created_at'