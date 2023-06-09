import httpx
from fastapi import HTTPException
from app.models.kong_consumer import KongConsumerAttributes, CreateKongConsumer, KongConsumer

async def create_kong_consumer(kong_consumer_to_be_created: CreateKongConsumer):
    """
    Asynchronous function to create a Kong consumer.

    The function sends a POST request to the Kong API to create a new consumer with the provided username and custom id.
    On successful creation, it returns the newly created consumer as a `KongConsumer` object.
    In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        kong_consumer_to_be_created (CreateKongConsumer): Object containing the username and custom id for the new consumer.

    Returns:
        KongConsumer: Object representing the newly created consumer in Kong.

    Raises:
        HTTPException: If the HTTP request returns an error code, the consumer already exists, or there is an issue while attempting to communicate with the Kong API.
    """
    try:
        kong_consumer = {
            KongConsumerAttributes.username.value: kong_consumer_to_be_created.username,
            KongConsumerAttributes.custom_id.value: kong_consumer_to_be_created.custom_id
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://kong:8001/consumers",
                data=kong_consumer
            )
        
        if response.status_code == 201:
            created_consumer = KongConsumer.parse_obj(response.json())
            return created_consumer
        
        if response.status_code == 409:
            raise HTTPException(status_code=409, detail="create_kong_consumer: Kong consumer already exists")
        else:
            raise HTTPException(status_code=500, detail=f"create_kong_consumer: {response.text}")

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"create_kong_consumer: {e}")