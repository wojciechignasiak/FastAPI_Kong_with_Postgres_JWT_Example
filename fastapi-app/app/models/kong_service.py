from pydantic import BaseModel
from enum import Enum

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
