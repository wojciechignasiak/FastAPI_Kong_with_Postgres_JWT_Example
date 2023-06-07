from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.models.kong_jwt import KongJWTCredentials
from app.kong.create_jwt_credential_for_consumer_using_username import create_jwt_credential_for_consumer_using_username
from app.generators.generate_jwt_with_username import generate_jwt_with_username

router = APIRouter()

@router.get("/get-jwt-token-for-consumer-using-username")
async def get_jwt_token_for_consumer_using_username_handler(consumer_username: str) -> JSONResponse:
    try:
        jwt_credential: KongJWTCredentials = await create_jwt_credential_for_consumer_using_username(kong_consumer_username = consumer_username)
        token = await generate_jwt_with_username(kong_consumer_username = consumer_username, kong_jwt_credential = jwt_credential)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=str(token)
        )
    except HTTPException as e:
        raise e
