import httpx
from fastapi import HTTPException

async def delete_kong_consumer_using_id(kong_consumer_id_to_be_deleted: str):
    """
    Asynchronous function to delete a Kong consumer using the consumer's id.

    The function sends a DELETE request to the Kong API to remove the specified consumer.
    If successful, it returns True. In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        kong_consumer_id_to_be_deleted (str): Identifier of the Kong consumer to be deleted.

    Returns:
        bool: True if the operation was successful and the consumer was deleted, False otherwise.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
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