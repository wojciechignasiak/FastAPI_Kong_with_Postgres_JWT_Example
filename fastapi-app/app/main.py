from fastapi import FastAPI
from app.routers import (
    create_kong_consumer,
    delete_kong_consumer_using_username,
    delete_kong_consumer_using_id,
    get_jwt_token_for_consumer_using_username,
    get_jwt_token_for_consumer_using_id,
    fastapi_bearer_authorization_and_jwt_payload_decoding,
    revoke_current_kong_consumer_jwt_using_id,
    revoke_current_kong_consumer_jwt_using_username,
    revoke_all_kong_consumer_jwt_using_id,
    revoke_all_kong_consumer_jwt_using_username,
    create_fastapi_app_service_in_kong,
    remove_fastapi_app_service_from_kong_using_id,
    remove_fastapi_app_service_from_kong_using_service_name
)

def create_application() -> FastAPI:
    application = FastAPI(openapi_url="/kong-manager/openapi.json", docs_url="/kong-manager/docs")
    #routers 
    application.include_router(create_kong_consumer.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(delete_kong_consumer_using_username.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(delete_kong_consumer_using_id.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(get_jwt_token_for_consumer_using_username.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(get_jwt_token_for_consumer_using_id.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(fastapi_bearer_authorization_and_jwt_payload_decoding.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(revoke_current_kong_consumer_jwt_using_id.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(revoke_current_kong_consumer_jwt_using_username.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(revoke_all_kong_consumer_jwt_using_id.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(revoke_all_kong_consumer_jwt_using_username.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(create_fastapi_app_service_in_kong.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(remove_fastapi_app_service_from_kong_using_id.router, prefix="/kong-manager", tags=["kong-manager"])
    application.include_router(remove_fastapi_app_service_from_kong_using_service_name.router, prefix="/kong-manager", tags=["kong-manager"])
    return application

#creating a global variable for the application
app = create_application()



@app.on_event("startup")
async def startup_event():
    print("fastapi-app started!")

@app.on_event("shutdown")
async def shutdown_event():
    print("fastapi-app stopped!")