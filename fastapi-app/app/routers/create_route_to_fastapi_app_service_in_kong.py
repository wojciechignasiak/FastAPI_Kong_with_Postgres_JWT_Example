from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.kong_route import CreateRouteForServiceInKong
from app.kong.create_route_to_fastapi_app_service_in_kong import create_route_to_fastapi_app_service_in_kong
router = APIRouter()

@router.post("/create-route-to-fastapi-app-service-in-kong")
async def create_route_to_fastapi_app_service_in_kong_handler(route: CreateRouteForServiceInKong) -> JSONResponse:
    try:
        response = await create_route_to_fastapi_app_service_in_kong(route = route)
        if response is not False:
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content=jsonable_encoder(response)
            )
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except HTTPException as e:
        raise e