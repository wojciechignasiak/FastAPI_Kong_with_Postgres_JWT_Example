import httpx
from fastapi import HTTPException
from app.models.kong_jwt import KongJWTCredentials



async def delete_all_kong_consumer_jwt_using_id(kong_consumer_id: str):
    """
    Asynchronous function to delete all JWT (JSON Web Token) credentials for a Kong consumer using its id.

    The function sends a GET request to the Kong API to retrieve all JWT credentials for the specified consumer.
    Then, it sends DELETE requests to remove each retrieved JWT credential.
    If successful, it returns True. If no JWT credentials were found or deleted, it returns False.
    In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        kong_consumer_id (str): Identifier of the Kong consumer for which the JWT credentials are to be deleted.

    Returns:
        bool: True if the operation was successful and JWT credentials were deleted, False otherwise.

    Raises:
        HTTPException: If there is an issue while attempting to communicate with the Kong API.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"http://kong:8001/consumers/{kong_consumer_id}/jwt"
            )
            if response.status_code == 200 and bool(response.json()['data']):
                list_of_jwt = response.json()['data']
                for jwt in list_of_jwt:
                    jwt_object: KongJWTCredentials = KongJWTCredentials.parse_obj(jwt)
                    response = await client.delete(
                        f"http://kong:8001/consumers/{kong_consumer_id}/jwt/{jwt_object.id}"
                    )
                return True
            else:
                return False

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_all_kong_consumer_jwt_using_id: {e}")