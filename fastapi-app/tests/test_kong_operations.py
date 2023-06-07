import pytest
import asyncio
from app.models.kong_consumer import CreateKongConsumer, KongConsumer
from app.models.kong_jwt import KongJWTCredentials, KongJWTConsumerParameter
from app.models.kong_service import CreateServiceInKong, ServiceInKong
from app.models.kong_route import CreateRouteForServiceInKong, RouteForService, ServiceInRouteResponse
from app.models.kong_plugin import KongPlugin, KongPluginClaim, PluginInService, ServiceInPluginResponse, ConfigInPluginResponse
from app.kong.create_kong_consumer import create_kong_consumer
from app.kong.delete_kong_consumer_using_id import delete_kong_consumer_using_id
from app.kong.delete_kong_consumer_using_username import delete_kong_consumer_using_username
from app.kong.add_exp_claim_to_verify_in_jwt import add_exp_claim_to_verify_in_jwt
from app.kong.add_jwt_plugin_to_service_in_kong import add_jwt_plugin_to_service_in_kong
from app.kong.create_fastapi_app_service_in_kong import create_fastapi_app_service_in_kong
from app.kong.create_jwt_credential_for_consumer_using_id import create_jwt_credential_for_consumer_using_id
from app.kong.create_jwt_credential_for_consumer_using_username import create_jwt_credential_for_consumer_using_username
from app.kong.create_route_to_fastapi_app_service_in_kong import create_route_to_fastapi_app_service_in_kong
from app.kong.delete_all_kong_consumer_jwt_using_id import delete_all_kong_consumer_jwt_using_id
from app.kong.delete_all_kong_consumer_jwt_using_username import delete_all_kong_consumer_jwt_using_username
from app.kong.delete_current_kong_consumer_jwt_using_id import delete_current_kong_consumer_jwt_using_id
from app.kong.delete_current_kong_consumer_jwt_using_username import delete_current_kong_consumer_jwt_using_username
from app.kong.delete_fastapi_app_service_from_kong_using_id import delete_fastapi_app_service_from_kong_using_id
from app.kong.delete_fastapi_app_service_from_kong_using_service_name import delete_fastapi_app_service_from_kong_using_service_name
from app.kong.delete_route_from_kong_using_id_or_name import delete_route_from_kong_using_id_or_name
from app.kong.delete_route_from_kong_associated_to_specific_service import delete_route_from_kong_associated_to_specific_service


consumer_ids = list()
consumer_usernames = list()
jwt_plugin_id = "id"
jwt_credentials_id = list()

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_create_kong_consumer(event_loop):
    global consumer_ids
    global consumer_usernames
    consumer: CreateKongConsumer = CreateKongConsumer(username="test_username", custom_id="test_custom_id")
    result: KongConsumer = await create_kong_consumer(consumer)
    consumer_ids.append(result.id)
    consumer_usernames.append(result.username)
    consumer_1: CreateKongConsumer = CreateKongConsumer(username="test_username_1", custom_id="test_custom_id_1")
    result_1: KongConsumer = await create_kong_consumer(consumer_1)
    consumer_ids.append(result_1.id)
    consumer_usernames.append(result_1.username)
    assert isinstance(result, KongConsumer)
    assert isinstance(result_1, KongConsumer)
    
@pytest.mark.asyncio
async def test_create_jwt_credential_for_consumer_using_id(event_loop):
    global jwt_credentials_id
    result: KongJWTCredentials = await create_jwt_credential_for_consumer_using_id(consumer_ids[0])
    jwt_credentials_id.append(result.id)
    assert isinstance(result, KongJWTCredentials)
    assert isinstance(result.consumer, KongJWTConsumerParameter)
    
@pytest.mark.asyncio
async def test_create_jwt_credential_for_consumer_using_username(event_loop):
    global jwt_credentials_id
    result: KongJWTCredentials = await create_jwt_credential_for_consumer_using_username(consumer_usernames[1])
    jwt_credentials_id.append(result.id)
    assert isinstance(result, KongJWTCredentials)
    assert isinstance(result.consumer, KongJWTConsumerParameter)

@pytest.mark.asyncio
async def test_create_fastapi_app_service_in_kong(event_loop):
    service_to_be_created: CreateServiceInKong = CreateServiceInKong(service_name="fastapi-app", service_url="http://fastapi-app:80/kong-fastapi-example")
    result = await create_fastapi_app_service_in_kong(service=service_to_be_created)
    assert isinstance(result, ServiceInKong)

@pytest.mark.asyncio
async def test_create_route_to_fastapi_app_service_in_kong(event_loop):
    route_to_be_created: CreateRouteForServiceInKong = CreateRouteForServiceInKong(route_name="kong-fastapi-example-route", service_name="fastapi-app", paths=["/kong-fastapi-example"])
    result = await create_route_to_fastapi_app_service_in_kong(route=route_to_be_created)
    assert isinstance(result, RouteForService)
    assert isinstance(result.service, ServiceInRouteResponse)

@pytest.mark.asyncio
async def test_add_jwt_plugin_to_service_in_kong(event_loop):
    global jwt_plugin_id
    plugin_to_be_added: KongPlugin = KongPlugin(plugin_name="jwt", service_name_or_id="fastapi-app")
    result = await add_jwt_plugin_to_service_in_kong(plugin_to_be_added)
    jwt_plugin_id = result.id
    assert isinstance(result, PluginInService)
    assert isinstance(result.service, ServiceInPluginResponse)
    assert isinstance(result.config, ConfigInPluginResponse)

@pytest.mark.asyncio
async def test_add_exp_claim_to_verify_in_jwt(event_loop):
    global jwt_plugin_id
    plugin_claim: KongPluginClaim = KongPluginClaim(plugin_id=jwt_plugin_id, claims_to_verify="exp")
    result = await add_exp_claim_to_verify_in_jwt(plugin_claim)
    assert isinstance(result, PluginInService)
    assert isinstance(result.service, ServiceInPluginResponse)
    assert isinstance(result.config, ConfigInPluginResponse)