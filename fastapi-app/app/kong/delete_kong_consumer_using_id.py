import httpx
from fastapi import HTTPException

async def delete_kong_consumer_using_id(kong_consumer_id_to_be_deleted: str):
    """Function to delete a kong consumer

    Args:
        kong_consumer_id_to_be_deleted (str): The id of the kong consumer to be deleted
    
    Raises:
        HTTPException: 500 If the delete request fails

    Returns:
        bool: True if the delete request succeeds. 
    
    Examples:
        >>> delete_kong_consumer_using_id("4f596ce5-f799-4bc7-9c54-cfc90c3eff42")
        True

    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://kong:8001/consumers/{kong_consumer_id_to_be_deleted}"
            )
            if response.status_code == 204:
                return True
            else:
                raise HTTPException(status_code=500, detail=f"delete_kong_consumer_using_id: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_kong_consumer_using_id: {e}")