from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.kong.revoke_all_kong_consumer_jwt_using_id import revoke_all_kong_consumer_jwt_using_id


router = APIRouter()

@router.delete("/revoke_all_kong_consumer_jwt_using_id")
async def revoke_all_kong_consumer_jwt_using_id_handler(consumer_id: str) -> JSONResponse:
    try:
        response = await revoke_all_kong_consumer_jwt_using_id(kong_consumer_id = consumer_id)
        if response==True:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "JWTs revoked successfully"}
            )
        else:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No JWTs to revoke"})
    except HTTPException as e:
        raise e