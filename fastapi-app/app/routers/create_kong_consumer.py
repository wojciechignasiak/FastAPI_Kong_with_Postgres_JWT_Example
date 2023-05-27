from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.models.kong_consumer import CreateKongConsumer, KongConsumer
from app.kong.create_kong_consumer import create_kong_consumer
router = APIRouter()

@router.post("/create_kong_consumer")
async def create_kong_consumer_handler(new_kong_consumer: CreateKongConsumer) -> JSONResponse:
    try:
        created_consumer: KongConsumer = await create_kong_consumer(kong_consumer_to_be_created = new_kong_consumer)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(created_consumer)
        )
    except HTTPException as e:
        raise e
