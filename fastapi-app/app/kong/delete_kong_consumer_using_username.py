import httpx
from fastapi import HTTPException

async def delete_kong_consumer_using_username(kong_consumer_username_to_be_deleted: str):
    """Function to delete a kong consumer

    Args:
        kong_consumer_username_to_be_deleted (str): The username of the kong consumer to be deleted
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://kong:8001/consumers/{kong_consumer_username_to_be_deleted}"
            )
            if response.status_code == 204:
                return True
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_kong_consumer_using_username: {e}")

