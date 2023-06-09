import httpx
from fastapi import HTTPException
from app.models.kong_service import CreateServiceInKong, ServiceInKongAttributes, ServiceInKong

async def create_fastapi_app_service_in_kong(service: CreateServiceInKong):
    """
    Asynchronous function to create a FastAPI application service within Kong.

    The function sends a POST request to the Kong API to create the service according to the provided data.
    On success, it returns the created service as a `ServiceInKong` object.
    In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        service (CreateServiceInKong): Object containing the service name and service URL for the new service.

    Returns:
        ServiceInKong: Object representing the newly created service in Kong.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
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