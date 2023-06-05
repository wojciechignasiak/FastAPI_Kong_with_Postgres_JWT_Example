import httpx
from fastapi import HTTPException

async def remove_fastapi_app_service_from_kong_using_id(service_id: str):
    """Function to remove fastapi-app service from kong.


    Args:
        service_id: The service to remove.

    Returns:
        True or False: If the service was removed.

    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://kong:8001/services/{service_id}")
        if response.is_success:
            return True
        else:
            return False
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"remove_fastapi_app_service_from_kong_using_id: {e}")