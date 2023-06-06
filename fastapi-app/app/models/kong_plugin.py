from pydantic import BaseModel
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
    