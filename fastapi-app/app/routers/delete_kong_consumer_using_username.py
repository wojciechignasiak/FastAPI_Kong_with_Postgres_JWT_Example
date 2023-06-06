from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.kong.delete_kong_consumer_using_username import delete_kong_consumer_using_username
router = APIRouter()

@router.delete("/delete-kong-consumer-using-username")
async def delete_kong_consumer_using_username_handler(kong_consumer_username: str) -> JSONResponse:
    try:
        response = await delete_kong_consumer_using_username(kong_consumer_username_to_be_deleted = kong_consumer_username)
        if response:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder({"message": "Kong consumer deleted successfully or consumer doesn't exists"})
            )
    except HTTPException as e:
        raise e
