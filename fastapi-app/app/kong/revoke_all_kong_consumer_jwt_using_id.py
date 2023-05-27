import httpx
from fastapi import HTTPException
from app.models.kong_jwt import KongJWTCredentials



async def revoke_all_kong_consumer_jwt_using_id(kong_consumer_id: str): 
    """Function to revoke all jwts of a kong consumer

    Args:
        kong_consumer_id (str): The id of the kong consumer to revoke jwts
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"http://kong:8001/consumers/{kong_consumer_id}/jwt"
            )
            if response.status_code == 200 and bool(response.json()['data']):
                list_of_jwt = response.json()['data']
                for jwt in list_of_jwt:
                    jwt_object: KongJWTCredentials = KongJWTCredentials(**jwt)
                    response = await client.delete(
                        f"http://kong:8001/consumers/{kong_consumer_id}/jwt/{jwt_object.id}"
                    )
                return True
            else:
                return False

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"revoke_all_kong_consumer_jwt_using_id: {e}")