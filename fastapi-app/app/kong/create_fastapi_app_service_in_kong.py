import httpx
from fastapi import HTTPException
from app.models.kong_service import CreateServiceInKong, ServiceInKongAttributes, ServiceInKong

async def create_fastapi_app_service_in_kong(service: CreateServiceInKong):
    """Function that adds fastapi-app service to kong.


    Args:
        service (CreateServiceInKong): The service to be created.

    Returns:
        ServiceInKong class: If the service was created.


    Raises:
        HTTPException: 500 if fail.
        
    Example:
        >>> create_fastapi_app_service_in_kong(CreateServiceInKong(service_name="fastapi-app", service_url="http://fastapi-app:80/kong-fastapi-example"))
        json

    """
    try:
        service_data = {
            ServiceInKongAttributes.service_name.value: service.service_name,
            ServiceInKongAttributes.service_url.value: service.service_url,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"http://kong:8001/services", data=service_data)
        if response.is_success:
            response: ServiceInKong = ServiceInKong.parse_obj(response.json())
            return response
        else:
            raise HTTPException(status_code=500, detail=f"create_fastapi_app_service_in_kong: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"create_fastapi_app_service_in_kong: {e}")