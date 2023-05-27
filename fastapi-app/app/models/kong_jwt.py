from pydantic import BaseModel
from enum import Enum

class KongJWTConsumerParameter(BaseModel):
    id: str


class KongJWTCredentials(BaseModel):
    consumer: KongJWTConsumerParameter
    tags: str = None
    id: str
    created_at: int
    algorithm: str
    secret: str
    rsa_public_key: str = None
    key: str


class KongJWTAttribures(str, Enum):
    kong_jwt_id = 'kong_jwt_id'
    id = 'id'
    key = 'key'
    secret = 'secret'
    tags = 'tags'
    created_at = 'created_at'
    algorithm = 'algorithm'
    consumer = 'consumer'
    rsa_public_key = 'rsa_public_key'