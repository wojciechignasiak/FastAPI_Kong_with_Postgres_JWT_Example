import httpx
from fastapi import HTTPException

async def delete_fastapi_app_service_from_kong_using_id(service_id: str):
    """
    Asynchronous function to delete a FastAPI application service from Kong using the service's id.

    The function sends a DELETE request to the Kong API to remove the specified service.
    If successful, it returns True. If the service cannot be deleted or does not exist, it returns False.
    In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        service_id (str): Identifier of the service to be deleted.

    Returns:
        bool: True if the operation was successful and the service was deleted, False otherwise.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
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