import httpx
from fastapi import HTTPException
from app.models.kong_jwt import KongJWTCredentials

async def create_jwt_credential_for_consumer_using_id(kong_consumer_id: str):
    """
    Asynchronous function to create a JWT (JSON Web Token) credential for a Kong consumer using its id.

    The function sends a POST request to the Kong API to create the JWT credential for the specified consumer.
    On success, it returns the created JWT credential as a `KongJWTCredentials` object.
    In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        kong_consumer_id (str): Identifier of the Kong consumer for which the JWT credential is to be created.

    Returns:
        KongJWTCredentials: Object representing the newly created JWT credential.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"http://kong:8001/consumers/{kong_consumer_id}/jwt")
        if response.is_success:
            created_jwt_credential: KongJWTCredentials = KongJWTCredentials.parse_obj(response.json())
            return created_jwt_credential
        else:
            raise HTTPException(status_code=500, detail=f"create_jwt_credential_for_consumer_using_id: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"create_jwt_credential_for_consumer_using_id: {e}")