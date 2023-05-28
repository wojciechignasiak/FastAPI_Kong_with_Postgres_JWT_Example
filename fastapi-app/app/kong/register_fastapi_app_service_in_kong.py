import httpx
from fastapi import HTTPException
from app.models.kong_service import RegisterServiceInKong, ServiceInKongAttributes

async def register_fastapi_app_service_in_kong(service: RegisterServiceInKong):
    """Function to add fastapi-app service to kong.


    Args:
        service (RegisterServiceInKong): The service to register.

    Returns:
        True or False: If the service was registered.

    """
    try:
        service_data = {
            ServiceInKongAttributes.service_name.value: service.service_name,
            ServiceInKongAttributes.service_url.value: service.service_url,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"http://kong:8001/services", data=service_data)
            print(response.json())
        if response.is_success:
            return True
        else:
            return False
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"register_fastapi_app_service_in_kong: {e}")