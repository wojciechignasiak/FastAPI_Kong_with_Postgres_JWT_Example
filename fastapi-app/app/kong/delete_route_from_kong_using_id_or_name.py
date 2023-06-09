import httpx
from fastapi import HTTPException

async def delete_route_from_kong_using_id_or_name(route_id_or_name_to_delete: str):
    """
    Asynchronous function to delete a route from Kong using its id or name.

    The function sends a DELETE request to the Kong API to remove the specified route.
    If successful, it returns True. In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        route_id_or_name_to_delete (str): Identifier or name of the route to be deleted.

    Returns:
        bool: True if the operation was successful and the route was deleted, False otherwise.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://kong:8001/routes/{route_id_or_name_to_delete}"
            )
            if response.status_code == 204:
                return True
            else:
                raise HTTPException(status_code=500, detail=f"delete_route_from_kong_using_id_or_name: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_route_from_kong_using_id_or_name: {e}")