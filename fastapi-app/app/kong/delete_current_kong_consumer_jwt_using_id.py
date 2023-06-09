import httpx
from fastapi import HTTPException

async def delete_current_kong_consumer_jwt_using_id(kong_consumer_id: str, kong_jwt_id: str):
    """
    Asynchronous function to delete a specific JWT (JSON Web Token) credential for a Kong consumer using its id.

    The function sends a DELETE request to the Kong API to remove the JWT credential of the specified consumer with the given JWT id.
    If successful, it returns True. In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        kong_consumer_id (str): Identifier of the Kong consumer for which the JWT credential is to be deleted.
        kong_jwt_id (str): Identifier of the JWT credential to be deleted.

    Returns:
        bool: True if the operation was successful and the JWT credential was deleted, False otherwise.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://kong:8001/consumers/{kong_consumer_id}/jwt/{kong_jwt_id}"
            )
            if response.status_code == 204:
                return True
            else:
                raise HTTPException(status_code=500, detail=f"delete_current_kong_consumer_jwt_using_id: {response.text}")
            
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_current_kong_consumer_jwt_using_id: {e}")