import httpx
from fastapi import HTTPException
from app.models.kong_service import CreateServiceInKong, ServiceInKongAttributes

async def create_fastapi_app_service_in_kong(service: CreateServiceInKong):
    """Function to add fastapi-app service to kong.


    Args:
        service (CreateServiceInKong): The service to create.

    Returns:
        json Kong response or False: If the service was created.

    """
    try:
        service_data = {
            ServiceInKongAttributes.service_name.value: service.service_name,
            ServiceInKongAttributes.service_url.value: service.service_url,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"http://kong:8001/services", data=service_data)
        if response.is_success:
            return response.json()
        else:
            return False
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"create_fastapi_app_service_in_kong: {e}")