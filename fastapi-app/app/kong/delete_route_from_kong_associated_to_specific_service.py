import httpx
from fastapi import HTTPException

async def delete_route_from_kong_associated_to_specific_service(route_id_or_name_to_delete: str, service_id_or_name: str):
    """Function to delete a route

    Args:
        delete_route_from_kong_using_id_or_name (str): The id or name of the route to be deleted
    
    Raises:
        HTTPException: 500 If the route could not be deleted

    Returns:
        bool: True if the route was deleted, False otherwise. 
    
    Examples:
        >>> delete_route_from_kong_associated_to_specific_service("route_id_or_name", "service_id_or_name")
        True
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://kong:8001/services/{service_id_or_name}/routes/{route_id_or_name_to_delete}"
            )
            if response.status_code == 204:
                return True
            else:
                return False
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_route_from_kong_associated_to_specific_service: {e}")