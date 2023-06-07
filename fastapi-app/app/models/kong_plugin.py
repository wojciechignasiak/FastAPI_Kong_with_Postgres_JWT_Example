from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum

class KongPlugin(BaseModel):
    plugin_name: str
    service_name_or_id: str
    
    class Config:
        schema_extra = {
            "example": {
                "plugin_name": "jwt",
                "service_name_or_id": "fastapi-app"
            }
        }

class KongPluginAttributes(str, Enum):
    plugin_name = "name"
    claims_to_verify = "config.claims_to_verify"


class KongPluginClaim(BaseModel):
    plugin_id: str
    claims_to_verify: str
    
    class Config:
        schema_extra = {
            "example": {
                "plugin_id": "xxx-xxx-xxx",
                "claims_to_verify": "exp"
            }
        }
    

class ServiceInPluginResponse(BaseModel):
    id: str

class ConfigInPluginResponse(BaseModel):
    uri_param_names: List[str]
    key_claim_name: str
    header_names: List[str]
    claims_to_verify: Optional[List[str]] = Field(None)
    maximum_expiration: int
    run_on_preflight: bool
    anonymous: Optional[str] = Field(None)
    secret_is_base64: bool
    cookie_names: List[str]

class PluginInService(BaseModel):
    protocols: List[str]
    created_at: int
    tags: Optional[List[str]] = Field(None)
    enabled: bool
    consumer: Optional[str] = Field(None)
    name: str
    id: str
    service: ServiceInPluginResponse
    config: ConfigInPluginResponse
    route: Optional[str] = Field(None)