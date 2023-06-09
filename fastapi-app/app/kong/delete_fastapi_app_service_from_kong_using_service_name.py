import httpx
from fastapi import HTTPException

async def delete_fastapi_app_service_from_kong_using_service_name(service_name: str):
    """
    Asynchronous function to delete a FastAPI application service from Kong using the service's name.

    The function sends a DELETE request to the Kong API to remove the specified service.
    If successful, it returns True. In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        service_name (str): Name of the service to be deleted.

    Returns:
        bool: True if the operation was successful and the service was deleted, False otherwise.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://kong:8001/services/{service_name}")
        if response.is_success:
            return True
        else:
            raise HTTPException(status_code=500, detail=f"delete_fastapi_app_service_from_kong_using_service_name: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_fastapi_app_service_from_kong_using_service_name: {e}")