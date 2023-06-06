from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from app.decoders.jwt_payload_decoder import jwt_payload_decoder
from app.kong.delete_current_kong_consumer_jwt_using_username import delete_current_kong_consumer_jwt_using_username


router = APIRouter()

@router.delete("/delete-current-consumer-jwt-using-username")
async def delete_current_consumer_jwt_using_username_handler(token: str = Depends(HTTPBearer())) -> JSONResponse:
    try:
        decoded_payload = await jwt_payload_decoder(token)
        response = await delete_current_kong_consumer_jwt_using_username(kong_consumer_username = decoded_payload["username"], kong_jwt_id = decoded_payload["kong_jwt_id"])
        if response:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "JWT deleted successfully",
                        "info": "Thats how you delete a consumer JWT. Usually you should implement this function when user logs out from your web app"}
            )
    except HTTPException as e:
        raise e