import httpx
from fastapi import HTTPException
from app.models.kong_plugin import KongPlugin, KongPluginAttributes, PluginInService


async def add_jwt_plugin_to_service_in_kong(kong_plugin_and_service: KongPlugin):
    """Function that add jwt pluging to selected service

    Args:
        kong_plugin_and_service (KongPlugin)): KongPlugin is class that contains plugin name and service id or name

    Returns:
        json if success, raise HTTPException if fail.

    Raises:
        HTTPException: 500 if fail.
        
    Example:
        >>> add_jwt_plugin_to_service_in_kong(KongPlugin(plugin_name="jwt", service_name_or_id="test"))
        json
        
    """
    try:

        plugin_data = {
            KongPluginAttributes.plugin_name.value: kong_plugin_and_service.plugin_name,
        } 
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"http://kong:8001/services/{kong_plugin_and_service.service_name_or_id}/plugins", data=plugin_data
            )
            if response.is_success:
                response: PluginInService = PluginInService.parse_obj(response.json())       
                return response
            else:
                raise HTTPException(status_code=500, detail=f"add_jwt_plugin_to_service_in_kong: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"add_jwt_plugin_to_service_in_kong: {e}")