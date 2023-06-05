import httpx
from fastapi import HTTPException

async def remove_fastapi_app_service_from_kong_using_service_name(service_name: str):
    """Function to remove fastapi-app service from kong.


    Args:
        service_name: The service to remove.

    Returns:
        True or False: If the service was removed.

    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://kong:8001/services/{service_name}")
        if response.is_success:
            return True
        else:
            return False
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"remove_fastapi_app_service_from_kong_using_service_name: {e}")