import httpx
from fastapi import HTTPException
from app.models.kong_plugin import KongPlugin, KongPluginAttributes, PluginInService


async def add_jwt_plugin_to_service_in_kong(kong_plugin_and_service: KongPlugin):
    """
    Asynchronous function to add JWT (JSON Web Token) plugin to a service within Kong.

    The function sends a POST request to the Kong API to add the plugin to the service according to the provided data.
    On success, it returns the created plugin as a `PluginInService` object.
    In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        kong_plugin_and_service (KongPlugin): Object containing Kong plugin name and service name or id.

    Returns:
        PluginInService: Object representing the newly created plugin in the service.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
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