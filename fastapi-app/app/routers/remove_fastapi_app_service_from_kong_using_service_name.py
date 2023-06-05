from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.kong.remove_fastapi_app_service_from_kong_using_service_name import remove_fastapi_app_service_from_kong_using_service_name
router = APIRouter()

@router.delete("/remove-fastapi-app-service-from-kong_using_service_name")
async def remove_fastapi_app_service_from_kong_using_service_name_handler(existing_service_name: str) -> JSONResponse:
    try:
        response = await remove_fastapi_app_service_from_kong_using_service_name(service_name = existing_service_name)
        if response == True:
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content=jsonable_encoder({"message": "Service removed successfully"})
            )
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except HTTPException as e:
        raise e