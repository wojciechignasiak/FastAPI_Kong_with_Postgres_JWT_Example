from fastapi import FastAPI
from app.routers import (
    create_kong_consumer,
    delete_kong_consumer_using_username,
    delete_kong_consumer_using_id,
    get_jwt_token_for_consumer_using_username,
    get_jwt_token_for_consumer_using_id,
    fastapi_bearer_authorization_and_jwt_payload_decoding,
    delete_current_kong_consumer_jwt_using_id,
    delete_current_kong_consumer_jwt_using_username,
    delete_all_kong_consumer_jwt_using_id,
    delete_all_kong_consumer_jwt_using_username,
    create_fastapi_app_service_in_kong,
    delete_fastapi_app_service_from_kong_using_id,
    delete_fastapi_app_service_from_kong_using_service_name,
    create_route_to_fastapi_app_service_in_kong,
    delete_route_from_kong_using_id_or_name,
    delete_route_from_kong_associated_to_specific_service,
    add_jwt_plugin_to_service_in_kong,
    add_exp_claim_to_verify_in_jwt
)

def create_application() -> FastAPI:
    application = FastAPI(openapi_url="/kong-fastapi-example/openapi.json", docs_url="/kong-fastapi-example/docs")
    #routers 
    application.include_router(create_kong_consumer.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_kong_consumer_using_username.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_kong_consumer_using_id.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(get_jwt_token_for_consumer_using_username.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(get_jwt_token_for_consumer_using_id.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(fastapi_bearer_authorization_and_jwt_payload_decoding.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_current_kong_consumer_jwt_using_id.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_current_kong_consumer_jwt_using_username.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_all_kong_consumer_jwt_using_id.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_all_kong_consumer_jwt_using_username.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(create_fastapi_app_service_in_kong.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_fastapi_app_service_from_kong_using_id.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_fastapi_app_service_from_kong_using_service_name.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(create_route_to_fastapi_app_service_in_kong.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_route_from_kong_using_id_or_name.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(delete_route_from_kong_associated_to_specific_service.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(add_jwt_plugin_to_service_in_kong.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    application.include_router(add_exp_claim_to_verify_in_jwt.router, prefix="/kong-fastapi-example", tags=["kong-fastapi-example"])
    return application

#creating a global variable for the application
app = create_application()



@app.on_event("startup")
async def startup_event():
    print("fastapi-app started!")

@app.on_event("shutdown")
async def shutdown_event():
    print("fastapi-app stopped!")