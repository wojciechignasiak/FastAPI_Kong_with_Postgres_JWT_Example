import httpx
from fastapi import HTTPException

async def delete_route_from_kong_using_id_or_name(route_id_or_name_to_delete: str):
    """Function to delete a route

    Args:
        delete_route_from_kong_using_id_or_name (str): The id or name of the route to be deleted

    Raises:
        HTTPException: 500

    Returns:
        >>> delete_route_from_kong_using_id_or_name("route_id_or_name")
        True
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