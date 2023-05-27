import httpx
from fastapi import HTTPException
from app.models.kong_jwt import KongJWTCredentials

async def create_jwt_credential_for_consumer_using_id(kong_consumer_id: str):
    """Function to create jwt credential for a consumer.

    This function will create a new jwt credential for a consumer.

    Args:
        kong_consumer_id (str): The id of the consumer.

    Returns:
        created_jwt_credential (KongJWTCredentials): The created jwt credential.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"http://kong:8001/consumers/{kong_consumer_id}/jwt")
        if response.is_success:
            created_jwt_credential: KongJWTCredentials = KongJWTCredentials(**response.json())
            return created_jwt_credential
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"create_jwt_credential_for_consumer_using_id: {e}")