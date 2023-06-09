import httpx
from fastapi import HTTPException
from app.models.kong_route import CreateRouteForServiceInKong, RouteForServiceInKongAttributes, RouteForService

async def create_route_to_fastapi_app_service_in_kong(route: CreateRouteForServiceInKong):
    """
    Asynchronous function to create a route to a FastAPI application service within Kong.

    The function sends a POST request to the Kong API to create the route according to the provided data.
    On success, it returns the created route as a `RouteForService` object.
    In case of an HTTP response error or request issues, it raises an `HTTPException`.

    Args:
        route (CreateRouteForServiceInKong): Object containing the route name and paths for the new route.

    Returns:
        RouteForService: Object representing the newly created route in the service.

    Raises:
        HTTPException: If the HTTP request returns an error code or there is an issue while attempting to communicate with the Kong API.
    """
    try:
        route_data = {
            RouteForServiceInKongAttributes.route_name.value: route.route_name,
            RouteForServiceInKongAttributes.paths.value: route.paths,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"http://kong:8001/services/{route.service_name}/routes", data=route_data)
        if response.is_success:
            response: RouteForService = RouteForService.parse_obj(response.json())
            return response
        else:
            raise HTTPException(status_code=500, detail=f"create_route_to_fastapi_app_service_in_kong: {response.text}")
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"create_route_to_fastapi_app_service_in_kong: {e}")