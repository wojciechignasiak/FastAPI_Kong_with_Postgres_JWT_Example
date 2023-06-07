import httpx
from fastapi import HTTPException
from app.models.kong_jwt import KongJWTCredentials



async def delete_all_kong_consumer_jwt_using_username(kong_consumer_username: str): 
    """Function to delete all jwts of a kong consumer

    Args:
        kong_consumer_username (str): The username of the kong consumer to delete jwts

    Raises:
        HTTPException: 500 if the request to kong fails

    Returns:
        bool: True if the request to kong was successful, False if not. 
        If the request to kong was successful, the function will delete all jwts of the kong consumer. 
        If the request to kong was not successful, the function will return False. 
        If the request to kong was successful, but the kong consumer has no jwts, the function will return True. 
        If the request to kong was successful, but the kong consumer has jwts, the function will delete all jwts of the kong consumer. 
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"http://kong:8001/consumers/{kong_consumer_username}/jwt"
            )
            if response.status_code == 200 and bool(response.json()['data']):
                list_of_jwt = response.json()['data']
                for jwt in list_of_jwt:
                    jwt_object: KongJWTCredentials = KongJWTCredentials.parse_obj(jwt)
                    response = await client.delete(
                        f"http://kong:8001/consumers/{kong_consumer_username}/jwt/{jwt_object.id}"
                    )
                return True
            else:
                return False

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"delete_all_kong_consumer_jwt_using_username: {e}")