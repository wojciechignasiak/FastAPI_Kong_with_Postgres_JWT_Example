from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.kong_service import CreateServiceInKong
from app.kong.create_fastapi_app_service_in_kong import create_fastapi_app_service_in_kong
router = APIRouter()

@router.post("/create-fastapi-app-service-in-kong")
async def create_fastapi_app_service_in_kong_handler(service: CreateServiceInKong) -> JSONResponse:
    try:
        response = await create_fastapi_app_service_in_kong(service = service)
        if response is not False:
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content=jsonable_encoder(response)
            )
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except HTTPException as e:
        raise e