import httpx
from fastapi import HTTPException

async def delete_route_from_kong_associated_to_specific_service(route_id_or_name_to_delete: str, service_id_or_name: str):
    """
    Asynchronous function to delete a route from Kong, which is associated with a specific service, using the route's id or name and the service's id or name.

    The function sends a DELETE request to the Kong API to remove the specified route.
    If successful, it returns True. In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        route_id_or_name_to_delete (str): Identifier or name of the route to be deleted.
        service_id_or_name (str): Identifier or name of the service associated with the route.

    Returns:
        bool: True if the operation was successful and the route was deleted, False otherwise.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://kong:8001/services/{service_id_or_name}/routes/{route_id_or_name_to_delete}"
            )
            if response.status_code == 204:
                return True
            else:
                raise HTTPException(status_code=500, detail=f"delete_route_from_kong_associated_to_specific_service: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_route_from_kong_associated_to_specific_service: {e}")