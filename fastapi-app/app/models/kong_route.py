from pydantic import BaseModel
from enum import Enum

class CreateRouteForServiceInKong(BaseModel):
    route_name: str
    service_name: str
    paths: list[str]
    
    class Config:
        schema_extra = {
            "example": {
                "route_name": "kong-fastapi-example-route",
                "service_name": "fastapi-app",
                "paths": ["/kong-fastapi-example"]
            }
        }

class RouteForServiceInKongAttributes(str, Enum):
    paths = 'paths[]'
    route_name = 'name'
    service_name = 'name'
    