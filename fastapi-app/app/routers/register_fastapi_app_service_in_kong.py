from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.kong_service import RegisterServiceInKong
from app.kong.register_fastapi_app_service_in_kong import register_fastapi_app_service_in_kong
router = APIRouter()

@router.post("/register-fastapi-app-service-in-kong")
async def register_fastapi_app_service_in_kong_handler(service: RegisterServiceInKong) -> JSONResponse:
    try:
        response = await register_fastapi_app_service_in_kong(service = service)
        if response == True:
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content=jsonable_encoder({"message": f"Service {service.service_name} successfully registered"})
            )
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except HTTPException as e:
        raise e