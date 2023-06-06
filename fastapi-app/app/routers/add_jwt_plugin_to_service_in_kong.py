from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.kong_plugin import KongPlugin
from app.kong.add_jwt_plugin_to_service_in_kong import add_jwt_plugin_to_service_in_kong

router = APIRouter()

@router.post("/add-jwt-plugin-to-service-in-kong")
async def add_jwt_plugin_to_service_in_kong_handler(kong_plugin_and_service: KongPlugin) -> JSONResponse:
    try:
        response = await add_jwt_plugin_to_service_in_kong(kong_plugin_and_service = kong_plugin_and_service)
        
        if response is not False:
            response_message = jsonable_encoder(response)
            info = {"info": f"Remember to save plugin id. If you open fastapi-app throught kong api gateway (http://localhost:8000/kong-fastapi-example) in your browser, you should see message : Unauthorized message"}
            how_to_verify = {"how to verify?": "First generate JWT token, then, you should install postman and send get request with bearer authentication to (http://localhost:8000/kong-fastapi-example/fastapi-bearer-authorization-and-jwt-payload-decoding) if you get your payload as response that means it works"}
            response_message.update(info)
            response_message.update(how_to_verify)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(response_message)
            )
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except HTTPException as e:
        raise e