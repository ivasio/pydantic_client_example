from common_models.models import Order
from fastapi import APIRouter
from petstore_httpx_client import AsyncApis, ApiClient
from pydantic import BaseSettings, HttpUrl, BaseModel

from .entities.orders_history import OrdersHistory
from .repositories.order import OrderRepository
from .repositories.order_info import OrderInfoRepository
from .use_cases.add_new_order import AddNewOrderUseCase
from .use_cases.get_all_orders import GetAllOrdersUseCase


class PetstoreClientConfig(BaseSettings):
    PETSTORE_SERVER_HOST: HttpUrl
    PETSTORE_SERVER_PORT: int

    @property
    def url(self) -> str:
        return f'{self.PETSTORE_SERVER_HOST}:{self.PETSTORE_SERVER_PORT}'


petstore_client_config = PetstoreClientConfig()

order_infos = OrderInfoRepository()

personal_page_router = APIRouter()


@personal_page_router.get(
    "/orders",
    tags=["orders"],
    summary="Get all the orders",
)
async def get_all_orders() -> OrdersHistory:
    return GetAllOrdersUseCase(order_infos)()


class AddNewOrderRequest(BaseModel):
    price: float
    pet_category: str
    order: Order


@personal_page_router.put(
    "/orders",
    tags=["orders"],
    summary="Place new order",
)
async def add_new_order(
        request: AddNewOrderRequest
) -> Order:
    orders = OrderRepository(
        AsyncApis(ApiClient(
            host=petstore_client_config.url,
        ))
    )
    return await AddNewOrderUseCase(order_infos, orders)(request)
