import httpx
from fastapi import HTTPException

async def delete_fastapi_app_service_from_kong_using_id(service_id: str):
    """Function to delete fastapi-app service from kong.


    Args:
        service_id: The service to delete.

    Returns:
        True or False: If the service was deleted.

    Raises:
        HTTPException: If the service was not deleted.
        
    Examples:
        >>> delete_fastapi_app_service_from_kong_using_id("fb035c05f-cb23-4cee-96bd-4a107f0970db")
        True
        
    Note:
        This function is not intended to be used directly.
        Use the `delete_fastapi_app_service_from_kong` function instead.

    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://kong:8001/services/{service_id}")
        if response.is_success:
            return True
        else:
            return False
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_fastapi_app_service_from_kong_using_id: {e}")