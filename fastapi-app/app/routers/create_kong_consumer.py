from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.kong_consumer import CreateKongConsumer, KongConsumer
from app.kong.create_kong_consumer import create_kong_consumer
router = APIRouter()

@router.post("/create-kong-consumer")
async def create_kong_consumer_handler(new_kong_consumer: CreateKongConsumer) -> JSONResponse:
    try:
        created_consumer: KongConsumer = await create_kong_consumer(kong_consumer_to_be_created = new_kong_consumer)
        response_message = jsonable_encoder(created_consumer)
        info = {"info": "Thats how you create a consumer. Remember that you cannot use custom_id to get, update or delete a consumer in Kong. It's used only to map users from your database."}
        response_message.update(info)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(response_message)
        )
    except HTTPException as e:
        raise e
