from fastapi import APIRouter

from .entities.orders_history import OrdersHistory
from .repositories.order_info import OrderInfoRepository
from .use_cases.get_all_orders import GetAllOrdersUseCase


personal_page_router = APIRouter()


@personal_page_router.get(
    "/orders",
    tags=["orders"],
    summary="Get all the orders",
)
async def get_all_orders() -> OrdersHistory:
    return GetAllOrdersUseCase(OrderInfoRepository())()
