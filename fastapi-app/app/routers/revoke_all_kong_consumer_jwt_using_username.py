from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.kong.revoke_all_kong_consumer_jwt_using_username import revoke_all_kong_consumer_jwt_using_username


router = APIRouter()

@router.delete("/revoke_all_kong_consumer_jwt_using_username")
async def revoke_all_kong_consumer_jwt_using_username_handler(consumer_username: str) -> JSONResponse:
    try:
        response = await revoke_all_kong_consumer_jwt_using_username(kong_consumer_username=consumer_username)
        if response==True:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "JWT revoked successfully"}
            )
        else:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No JWTs to revoke"})
    except HTTPException as e:
        raise e