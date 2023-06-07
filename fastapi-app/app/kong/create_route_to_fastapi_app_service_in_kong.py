import httpx
from fastapi import HTTPException
from app.models.kong_route import CreateRouteForServiceInKong, RouteForServiceInKongAttributes, RouteForService

async def create_route_to_fastapi_app_service_in_kong(route: CreateRouteForServiceInKong):
    """Function that adds route fastapi-app service in kong.


    Args:
        route (CreateRouteForServiceInKong): The route to create.

    Returns:
        json Kong response or False: If the route was created.

    Raises:
        HTTPException: 500 If the route was not created.

    Examples:
        >>> create_route_to_fastapi_app_service_in_kong(CreateRouteForServiceInKong(route_name="test", service_name="fastapi-app", paths=["/test"]))
        >>> {
            "destinations": null,
            "hosts": null,
            "request_buffering": true,
            "response_buffering": true,
            "name": "test",
            "headers": null,
            "https_redirect_status_code": 426,
            "regex_priority": 0,
            "service": {
                "id": "b035c05f-cb23-4cee-96bd-4a107f0970db"
            },
            "id": "76fea7fc-f78b-4713-8f6e-9bb2e5ce9270",
            "tags": null,
            "path_handling": "v0",
            "protocols": [
                "http",
                "https"
            ],
            "preserve_host": false,
            "created_at": 1686061678,
            "updated_at": 1686061678,
            "snis": null,
            "strip_path": true,
            "paths": [
                "/test"
            ],
            "methods": null,
            "sources": null
            }
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