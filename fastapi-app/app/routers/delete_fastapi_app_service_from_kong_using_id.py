from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.kong.delete_fastapi_app_service_from_kong_using_id import delete_fastapi_app_service_from_kong_using_id
router = APIRouter()

@router.delete("/delete-fastapi-app-service-from-kong-using-id")
async def delete_fastapi_app_service_from_kong_using_id_handler(existing_service_id: str) -> JSONResponse:
    try:
        response = await delete_fastapi_app_service_from_kong_using_id(service_id = existing_service_id)
        if response == True:
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content=jsonable_encoder({"message": "Service deleted successfully"})
            )
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except HTTPException as e:
        raise e