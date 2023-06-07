from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class CreateServiceInKong(BaseModel):
    service_name: str
    service_url: str
    
    class Config:
        schema_extra = {
            "example": {
                "service_name": "fastapi-app",
                "service_url": "http://fastapi-app:80/kong-fastapi-example"
            }
        }

class ServiceInKongAttributes(str, Enum):
    service_name = 'name'
    service_url = 'url'


class ServiceInKong(BaseModel):
    enabled: bool
    created_at: int
    updated_at: int
    tls_verify: Optional[bool] = Field(None)
    tls_verify_depth: Optional[int] = Field(None)
    id: str
    retries: int
    path: str
    port: int
    tags: Optional[str] = Field(None)
    ca_certificates: Optional[str] = Field(None)
    name: str
    client_certificate: Optional[str] = Field(None)
    protocol: str
    connect_timeout: int
    host: str
    read_timeout: int
    write_timeout: int
