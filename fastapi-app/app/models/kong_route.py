from pydantic import BaseModel, Field
from typing import Optional, List
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
    

class ServiceInRouteResponse(BaseModel):
    id: str

class RouteForService(BaseModel):
    protocols: List[str]
    created_at: int
    updated_at: int
    strip_path: bool
    headers: Optional[str] = Field(None)
    name: str
    id: str
    service: ServiceInRouteResponse
    snis: Optional[str] = Field(None)
    request_buffering: bool
    response_buffering: bool
    paths: List[str]
    methods: Optional[str] = Field(None)
    https_redirect_status_code: int
    destinations: Optional[str] = Field(None)
    regex_priority: int
    sources: Optional[str] = Field(None)
    hosts: Optional[str] = Field(None)
    tags: Optional[str] = Field(None)
    path_handling: str
    preserve_host: bool