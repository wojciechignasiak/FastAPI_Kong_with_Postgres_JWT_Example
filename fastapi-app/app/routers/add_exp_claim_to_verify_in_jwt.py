from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.kong_plugin import KongPluginClaim
from app.kong.add_exp_claim_to_verify_in_jwt import add_exp_claim_to_verify_in_jwt

router = APIRouter()

@router.post("/add-exp-claim-to-verify-in-jwt")
async def add_exp_claim_to_verify_in_jwt_handler(kong_plugin_id_and_claim: KongPluginClaim) -> JSONResponse:
    try:
        response = await add_exp_claim_to_verify_in_jwt(kong_plugin_id_and_claim = kong_plugin_id_and_claim)
        
        if response is not False:
            response_message = jsonable_encoder(response)
            info = {"info": f"exp claim allows you to introduce a token expiration time mechanism. The lifetime of the jwt token is set when it is created."}
            response_message.update(info)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(response_message)
            )
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except HTTPException as e:
        raise e