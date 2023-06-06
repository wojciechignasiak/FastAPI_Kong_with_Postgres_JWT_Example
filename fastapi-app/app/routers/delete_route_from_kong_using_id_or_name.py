from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.kong.delete_route_from_kong_using_id_or_name import delete_route_from_kong_using_id_or_name

router = APIRouter()

@router.delete("/delete-route-from-kong-using-id-or-name")
async def delete_route_from_kong_using_id_or_name_handler(route_id_or_name: str) -> JSONResponse:
    try:
        response = await delete_route_from_kong_using_id_or_name(route_id_or_name_to_delete = route_id_or_name)
        if response:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder({"message": "Route deleted successfully"})
            )
    except HTTPException as e:
        raise e