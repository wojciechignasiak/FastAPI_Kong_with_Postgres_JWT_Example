import httpx
from fastapi import HTTPException
from app.models.kong_plugin import KongPluginClaim, KongPluginAttributes, PluginInService


async def add_exp_claim_to_verify_in_jwt(kong_plugin_id_and_claim: KongPluginClaim):
    """
    Asynchronous function to add claims to verify in JWT (JSON Web Token) within Kong service.

    The function sends a PATCH request to the Kong API to update the plugin according to the provided data.
    On success, it returns the updated plugin as a `PluginInService` object.
    In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        kong_plugin_id_and_claim (KongPluginClaim): Object containing Kong plugin identifier and claims to verify.

    Returns:
        PluginInService: Object representing the updated plugin in the service.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
    """
    try:
        claim_data = {
            KongPluginAttributes.claims_to_verify.value: kong_plugin_id_and_claim.claims_to_verify,
        } 
        async with httpx.AsyncClient() as client:
            response = await client.patch(
                f"http://kong:8001/plugins/{kong_plugin_id_and_claim.plugin_id}", data=claim_data 
            )
            if response.is_success:
                response: PluginInService = PluginInService.parse_obj(response.json())
                return response
            else:
                raise HTTPException(status_code=500, detail=f"add_exp_claim_to_verify_in_jwt: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"add_exp_claim_to_verify_in_jwt: {e}")