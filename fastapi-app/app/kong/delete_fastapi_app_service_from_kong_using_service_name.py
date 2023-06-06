import httpx
from fastapi import HTTPException

async def delete_fastapi_app_service_from_kong_using_service_name(service_name: str):
    """Function to delete fastapi-app service from kong.


    Args:
        service_name: The service to delete.

    Returns:
        True or False: If the service was deleted.

    Raises:
        HTTPException: 500.

    Examples:
        >>> delete_fastapi_app_service_from_kong_using_service_name("fastapi-app")
        True

    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://kong:8001/services/{service_name}")
        if response.is_success:
            return True
        else:
            return False
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_fastapi_app_service_from_kong_using_service_name: {e}")