import httpx
from fastapi import HTTPException
from app.models.kong_plugin import KongPluginClaim, KongPluginAttributes


async def add_exp_claim_to_verify_in_jwt(kong_plugin_id_and_claim: KongPluginClaim):
    """Function that add claim to jwt plugin

    Args:
        kong_plugin_id_and_claim (KongPluginClaim): KongPluginClaim is class that contains plugin id and claim to verify

    Returns:
        json if success, raise HTTPException if fail.

    Raises:
        HTTPException: 500 if fail.
        
    Example:
        >>> add_exp_claim_to_verify_in_jwt(KongPluginClaim(plugin_id="xxx-xxx-xxx", claim_to_verify="exp"))
        json
        
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
                return response.json()
            else:
                raise HTTPException(status_code=500, detail=f"add_exp_claim_to_verify_in_jwt: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"add_exp_claim_to_verify_in_jwt: {e}")