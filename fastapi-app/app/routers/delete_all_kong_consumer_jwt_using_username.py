from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.kong.delete_all_kong_consumer_jwt_using_username import delete_all_kong_consumer_jwt_using_username


router = APIRouter()

@router.delete("/delete-all-kong-consumer-jwt-using-username")
async def delete_all_kong_consumer_jwt_using_username_handler(consumer_username: str) -> JSONResponse:
    try:
        response = await delete_all_kong_consumer_jwt_using_username(kong_consumer_username=consumer_username)
        if response==True:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "JWTs deleted successfully",
                        "info": "Thats how you delete a consumer JWT. Usually you should implement this function when user use option logs out from all devices in your web app"}
            )
        else:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No JWTs to delete"})
    except HTTPException as e:
        raise e