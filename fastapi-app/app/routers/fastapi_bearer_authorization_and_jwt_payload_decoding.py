from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from app.decoders.jwt_payload_decoder import jwt_payload_decoder


router = APIRouter()

@router.get("/fastapi_bearer_authorization_and_jwt_payload_decoding")
async def fastapi_bearer_authorization_and_jwt_payload_decoding_handler(token: str = Depends(HTTPBearer())) -> JSONResponse:
    try:
        decoded_payload = await jwt_payload_decoder(token)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(decoded_payload)
        )
    except HTTPException as e:
        raise e