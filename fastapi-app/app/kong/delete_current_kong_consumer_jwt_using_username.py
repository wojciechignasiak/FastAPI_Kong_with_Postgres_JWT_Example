import httpx
from fastapi import HTTPException

async def delete_current_kong_consumer_jwt_using_username(kong_consumer_username: str, kong_jwt_id: str): 
    """Function to delete a current jwt of a kong consumer

    Args:
        kong_consumer_username (str): The username of the kong consumer to delete jwt
        kong_consumer_jwt_id (str): The id of current JWT credentials
    
    Returns:
        bool: True if the jwt was deleted.
    
    Raises:
        HTTPException: 500 
    
    Examples:
        >>> delete_current_kong_consumer_jwt_using_username("XXXXXXXXXXXXX", "test_jwt")
        True
    
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://kong:8001/consumers/{kong_consumer_username}/jwt/{kong_jwt_id}"
            )
            if response.status_code == 204:
                return True
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_current_kong_consumer_jwt_using_username: {e}")