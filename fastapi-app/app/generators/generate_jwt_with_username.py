import time
import jwt
from fastapi import HTTPException
from app.models.kong_jwt import KongJWTCredentials, KongJWTAttribures
from app.models.kong_consumer import KongConsumerAttributes

async def generate_jwt_with_username(kong_consumer_username: str, kong_jwt_credential: KongJWTCredentials):
    try:
        header_data = {
            "alg": kong_jwt_credential.algorithm,
            "typ": "JWT",
            "iss": kong_jwt_credential.key
        }
        payload_data = {
            KongConsumerAttributes.username.value: kong_consumer_username,
            KongJWTAttribures.kong_jwt_id.value: kong_jwt_credential.id,
            "exp": time.time() + 60
        }
        token = jwt.encode(
            payload=payload_data,
            key=kong_jwt_credential.key,
            headers=header_data
        )

        return token
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"generate_jwt_with_username: {e}")