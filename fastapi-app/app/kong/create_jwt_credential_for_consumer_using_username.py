import httpx
from fastapi import HTTPException
from app.models.kong_jwt import KongJWTCredentials

async def create_jwt_credential_for_consumer_using_username(kong_consumer_username: str):
    """Function to create jwt credential for a consumer.

    This function will create a new jwt credential for a consumer.

    Args:
        kong_consumer_username (str): The username of the consumer.

    Returns:
        created_jwt_credential (KongJWTCredentials): The created jwt credential.

    Raises:
        HTTPException: 500 if fail.
        
    Example:
        >>> create_jwt_credential_for_consumer_using_username(kong_consumer_username="my_username")
        json
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"http://kong:8001/consumers/{kong_consumer_username}/jwt")
        if response.is_success:
            created_jwt_credential: KongJWTCredentials = KongJWTCredentials(**response.json())
            return created_jwt_credential
        else:
            raise HTTPException(status_code=500, detail=f"create_jwt_credential_for_consumer_using_username: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"create_jwt_credential_for_consumer_using_username: {e}")