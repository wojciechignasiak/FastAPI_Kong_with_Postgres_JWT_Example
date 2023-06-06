import httpx
from fastapi import HTTPException

async def delete_current_kong_consumer_jwt_using_id(kong_consumer_id: str, kong_jwt_id: str): 
    """Function to delete a current jwt of a kong consumer

    Args:
        kong_consumer_id (str): The id of the kong consumer to delete jwt
        kong_consumer_jwt_id (str): The id of current JWT credentials
    
    Returns:
        bool: True if the jwt has been deleted.

    Raises:
        HTTPException: 500 if the request failed. 

    Examples:
        >>> delete_current_kong_consumer_jwt_using_id(kong_consumer_id="my_consumer_id", kong_jwt_id="my_jwt_id")
        True
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://kong:8001/consumers/{kong_consumer_id}/jwt/{kong_jwt_id}"
            )
            if response.status_code == 204:
                return True

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_current_kong_consumer_jwt_using_id: {e}")