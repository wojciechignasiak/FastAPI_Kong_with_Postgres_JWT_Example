from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.kong_jwt import KongJWTCredentials
from app.kong.create_jwt_credential_for_consumer_using_id import create_jwt_credential_for_consumer_using_id
from app.generators.generate_jwt_with_id import generate_jwt_with_id

router = APIRouter()

@router.get("/get_jwt_token_for_consumer_using_id")
async def get_jwt_token_for_consumer_using_id_handler(consumer_id: str) -> JSONResponse:
    try:
        jwt_credential: KongJWTCredentials = await create_jwt_credential_for_consumer_using_id(kong_consumer_id = consumer_id)
        token = await generate_jwt_with_id(kong_consumer_id = consumer_id, kong_jwt_credential = jwt_credential)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=str(token)
        )
    except HTTPException as e:
        raise e
