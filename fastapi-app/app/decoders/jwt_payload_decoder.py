import jwt
from fastapi import HTTPException

async def jwt_payload_decoder(token: str):
    try:
        decoded_token = jwt.decode(token.credentials, options={"verify_signature": False})
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"jwt_payload_decoder: {e}")