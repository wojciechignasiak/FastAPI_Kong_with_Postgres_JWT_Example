from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.kong.delete_kong_consumer_using_id import delete_kong_consumer_using_id

router = APIRouter()

@router.delete("/delete-kong-consumer-using-id")
async def delete_kong_consumer_using_id_handler(kong_consumer_id: str) -> JSONResponse:
    try:
        response = await delete_kong_consumer_using_id(kong_consumer_id_to_be_deleted = kong_consumer_id)
        if response:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder({"message": "Kong consumer deleted successfully or consumer doesn't exists"})
            )
    except HTTPException as e:
        raise e